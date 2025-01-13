function uploadWord() {
    var fileInput = document.getElementById("fileInput");
    var passwordInput = document.getElementById("passwordInput");
    var loadingSpinner = document.getElementById("loadingSpinner");

    var file = fileInput.files[0];
    var password = passwordInput.value;

    var formData = new FormData();
    formData.append("file", file);
    formData.append("password", password);

    var xhr = new XMLHttpRequest();

    loadingSpinner.style.display = "inline";  // Show loading spinner

    xhr.upload.onprogress = function (e) {
        if (e.lengthComputable) {
            var percentComplete = (e.loaded / e.total) * 100;
            document.getElementById("progressBar").style.width = percentComplete + '%';
        }
    };

    xhr.onload = function () {
        loadingSpinner.style.display = "none";  // Hide loading spinner

        if (xhr.status === 200) {
            document.getElementById("progressBar").innerText = "Complete! Click to download file";
            document.getElementById("progressBar").style.backgroundColor = "#008000";
        } else {
            document.getElementById("progressBar").innerText = "Upload failed. Check the file and try again.";
            document.getElementById("progressBar").style.backgroundColor = "#FF0000";
        }
    };

    xhr.open("POST", "/upload", true);
    xhr.send(formData);
}

function downloadFile() {
    var protectedFileName = "content_protected.docx";  // Update with your actual filename
    window.location.href = "/protected/" + protectedFileName;
}
