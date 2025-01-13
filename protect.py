import win32com.client
import pyautogui
import os
import easygui
import pygetwindow as gw
from PyQt5.QtWidgets import QApplication, QInputDialog
import time
import pywinauto


def focus_to_window(window_title=None):
    word_window = gw.getWindowsWithTitle(window_title)[0]
    if word_window.isActive == False:
        pywinauto.application.Application().connect(handle=word_window._hWnd).top_window().set_focus()
    if not word_window.isMaximized:
            word_window.maximize()
def maximize_word_window():
    try:
        pyautogui.getW
        word_window = gw.getWindowsWithTitle('Word')[0]
        if not word_window.isMaximized:
            word_window.maximize()
    except Exception as e:
        print(f"Lỗi khi kích hoạt cửa sổ Word: {e}")

def getPath(fileName):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), fileName)

def clickEffect(checkbox_location):
    if checkbox_location:
        x, y, width, height = checkbox_location
        center_x, center_y = x + width // 2, y + height // 2
        pyautogui.click(center_x, center_y, interval=0.1)
        return (center_x, center_y)
    else:
        print('Không tìm thấy ô tích.')
        return None

def denyEdit(password):
    try:
        imgReviewBlack = getPath("./assets/denyEdit/btnReviewB.png")
        imgReviewWhite = getPath("./assets/denyEdit/btnReviewW.png")
        btnReviewBlack = pyautogui.locateOnScreen(image=imgReviewBlack, minSearchTime=2)
        btnReviewWhite = pyautogui.locateOnScreen(image=imgReviewWhite, minSearchTime=2)
        if btnReviewBlack:
            clickEffect(btnReviewBlack)

            imgRestrictEditingBlack=getPath("./assets/denyEdit/btnRestrictEditingB.png")
            btnRestrictEditingBlack = pyautogui.locateOnScreen(image=imgRestrictEditingBlack, minSearchTime=1)
            clickEffect(btnRestrictEditingBlack)
            
            imgReadOnlyBlack = getPath("./assets/denyEdit/btnReadOnlyB.png")
            btnReadOnlyBlack = pyautogui.locateOnScreen(image=imgReadOnlyBlack, minSearchTime=1)
            clickEffect(btnReadOnlyBlack)

            imgStartProtectBlack = getPath("./assets/denyEdit/btnStartProtectB.png")
            btnStattProtectBlack = pyautogui.locateOnScreen(image=imgStartProtectBlack, minSearchTime=1)
            clickEffect(btnStattProtectBlack)

            pyautogui.write(password); 
            pyautogui.press("tab"); 
            pyautogui.write(password); 
            pyautogui.press(["tab", "enter"])
        elif btnReviewWhite :
            clickEffect(btnReviewWhite)

            imgRestrictEditingWhite=getPath("./assets/denyEdit/btnRestrictEditingW.png")
            btnRestrictEditingWhite = pyautogui.locateOnScreen(image=imgRestrictEditingWhite, minSearchTime=1)
            clickEffect(btnRestrictEditingWhite)

            imgReadOnlyWhite = getPath("./assets/denyEdit/btnReadOnlyW.png")
            btnReadOnlyWhite = pyautogui.locateOnScreen(image=imgReadOnlyWhite, minSearchTime=1)
            clickEffect(btnReadOnlyWhite)

            imgStartProtectWhite = getPath("./assets/denyEdit/btnStartProtectW.png")
            btnStartProtectWhite = pyautogui.locateOnScreen(image=imgStartProtectWhite, minSearchTime=1)
            clickEffect(btnStartProtectWhite)

            pyautogui.write(password)
            pyautogui.press("tab")
            pyautogui.write(password)
            pyautogui.press(["tab", "enter"])
        else:
            easygui.msgbox("Cần chuyển theme word sang Black, hoặc ColorFull và khởi động lại tool", title="Thông báo")
    except:
        easygui.msgbox("Cần khởi động lại tool", title="Thông báo")

def draw_shape_to_word_center():
    centerWord = (950, 550)
    pyautogui.move(centerWord, duration=0.2)
    pyautogui.click(centerWord, duration=0.2, button='left')
    pyautogui.dragTo(930, 530, duration=0.2, button='left')

def denyCopy(numberPages):
    try:
        viewOnePage=["alt","w", "1"]
        viewPage100=["alt", "w", "j"]
        for key in viewOnePage: pyautogui.press(key,interval=0.1)
        for key in viewPage100: pyautogui.press(key,interval=0.1)

        for page in range(numberPages):
            pyautogui.hotkey("alt", "n",interval=0.15)
            pyautogui.press("s",interval=0.15)
            pyautogui.press("h",interval=0.15)
            pyautogui.move(280, 400, duration=0.15)
            pyautogui.click(280, 400, clicks=1, interval=0.15, button='left')
            draw_shape_to_word_center()
            imgShapeEdit=getPath("./assets/denyCopy/btnEditShape.png")
            btnShapeEdit=pyautogui.locateOnScreen(image=imgShapeEdit, minSearchTime=1)
            clickEffect(btnShapeEdit)
            imgSeeMoreBlack=getPath("./assets/denyCopy/btnSeeMoreB.png")
            imgSeeMoreWhite=getPath("./assets/denyCopy/btnSeeMoreW.png")
            btnSeeMoreBlack=pyautogui.locateOnScreen(image=imgSeeMoreBlack,minSearchTime=1)
            btnSeeMoreWhite=pyautogui.locateOnScreen(image=imgSeeMoreWhite,minSearchTime=1)
            btnSeeMore = btnSeeMoreBlack if btnSeeMoreBlack else btnSeeMoreWhite
            clickEffect(btnSeeMore)

            shapePosition = ['tab', 'tab', 'a', 'tab', 'l', 'tab', 'p', 'tab', 'up', 'tab', 't', 'tab', 'p']
            for key in shapePosition:
                pyautogui.press(key, interval=0.15)

            imgSizeShape=getPath("./assets/denyCopy/btnSize.png")
            btnSizeShape=pyautogui.locateOnScreen(image=imgSizeShape, minSearchTime=1)
            clickEffect(btnSizeShape)

            shapeSize1 = ['tab', 'down', 'tab']
            for key in shapeSize1:
                pyautogui.press(key, interval=0.15)
            pyautogui.write("100")
            shapeSize2 = ['tab', 'p', 'tab', 'down', 'tab']
            for key in shapeSize2:
                pyautogui.press(key, interval=0.15)
            pyautogui.write("100")
            shapeSize3 = ['tab', 'p', 'tab', 'tab', 'tab', 'tab', 'tab', 'enter']
            for key in shapeSize3:
                pyautogui.press(key, interval=0.15)

            shapeFill=["alt","j","d","s","f","n"]
            shapeOutline=["alt","j","d","s","o","n"]
            for key in shapeFill:
                pyautogui.press(key,interval=0.15)
            for key in shapeOutline:
                pyautogui.press(key,interval=0.15)
            if page!=(numberPages-1):
                pyautogui.hotkey("ctrl","pagedown")
    except:
        easygui.msgbox("Cần chuyển theme word sang Black, hoặc ColorFull và khởi động lại tool", title="Thông báo")

def open_word_document(file_path):
    word_app = win32com.client.Dispatch("Word.Application")
    doc = word_app.Documents.Open(file_path)
    word_app.Visible = True
    return word_app, doc

def protect_word(file_path, password):
    # doc_path = getPath("docx/tailieumat.docx")

    doc_path=getPath(file_path)
    word_app, word_doc = open_word_document(doc_path)
    word_doc.Repaginate()
    num_of_sheets = word_doc.ComputeStatistics(2)
    focus_to_window("Word")
    denyCopy(num_of_sheets)
    denyEdit(password)
    newName = doc_path.split(".")
    # Define the protected file path
    
    word_doc.SaveAs(getPath("protected")+"/content_protected.docx" )

    word_doc.Close()
    word_app.Quit()
    
if __name__ == "__main__":
    protect_word(None, None)
