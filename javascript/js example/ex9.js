const captchaTextBox = document.querySelector(".captcha_box input");
const refreshButton = document.querySelector(".refresh_button");
const captchaInputBox = document.querySelector(".captcha_input input");
const message = document.querySelector(".message");
const submitButton = document.querySelector(".button");

let captchaText = "";

const generateCaptcha = () => {
    const randomString = Math.random().toString(36).substring(2, 7);
    const randomStringArray = randomString.split("");
    const changeString = randomStringArray.map(char => Math.random() > 0.5 ? char.toUpperCase() : char);
    
    captchaText = changeString.join(""); // Keep as a clean string (no spaces)
    captchaTextBox.value = captchaText; // Show in input box
    console.log("Generated Captcha: ", captchaText);
};

const refreshBtnClick = () => {
    generateCaptcha();
    captchaInputBox.value = "";
    captchaKeyupValidate();
};

const captchaKeyupValidate = () => {
    submitButton.classList.toggle("disabled", !captchaInputBox.value);
    if (captchaInputBox.value === "") message.classList.remove("active");
};

const submitBtnClick = () => {
    const enteredCaptcha = captchaInputBox.value.trim(); // Remove extra spaces
    
    message.classList.add("active");
    if (enteredCaptcha.toLowerCase() === captchaText.toLowerCase()) { // Case insensitive comparison
        message.innerText = "Entered CAPTCHA is correct ✅";
        message.style.color = "#28A745"; // Green color for success
    } else {
        message.innerText = "Entered CAPTCHA is incorrect ❌";
        message.style.color = "#FF2525"; // Red color for failure
    }
};

refreshButton.addEventListener("click", refreshBtnClick);
captchaInputBox.addEventListener("keyup", captchaKeyupValidate);
submitButton.addEventListener("click", submitBtnClick);

generateCaptcha();
