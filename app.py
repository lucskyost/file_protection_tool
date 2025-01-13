from flask import Flask, render_template, request, send_file, send_from_directory
from werkzeug.utils import secure_filename
import os
import pythoncom
import threading
from protect import protect_word

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
PROTECTED_FOLDER = 'protected'
ALLOWED_EXTENSIONS = {'docx'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROTECTED_FOLDER'] = PROTECTED_FOLDER

# Lock for COM operations
com_lock = threading.Lock()

def allowed_file(filename):
    return '.' in filename and filename.lower().rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

def protect_word_threaded(file_path, password):
    # Initialize COM for each thread
    pythoncom.CoInitialize()
    
    with com_lock:
        print("Tên file:", file_path, "Pass", password)
        return protect_word(file_path, password)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files or 'password' not in request.form:
        return "Missing file or password", 400

    file = request.files['file']
    password = request.form['password']

    if file.filename == '':
        return "No selected file", 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        thread = threading.Thread(target=protect_word_threaded, args=(file_path, password))
        thread.start()
        thread.join()

        return "File processing in progress"

    return "Invalid file or password", 400

@app.route('/protected/<filename>')
def protected(filename):
    return send_from_directory(app.config['PROTECTED_FOLDER'], filename)

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    if not os.path.exists(app.config['PROTECTED_FOLDER']):
        os.makedirs(app.config['PROTECTED_FOLDER']) 
    app.run(debug=True)
