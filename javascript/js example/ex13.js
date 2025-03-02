let passwordInput = document.getElementById("password");
let eyeIcon = document.getElementById("eyeicon");

eyeIcon.onclick = function () {
    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        eyeIcon.src = "image/eye-open.png"; // Change to open-eye image
    } else {
        passwordInput.type = "password";
        eyeIcon.src = "image/eye-close.png"; // Change back to closed-eye image
    }
};