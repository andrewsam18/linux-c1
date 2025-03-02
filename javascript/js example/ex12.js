const passwordBox = document.getElementById("Password"); // Corrected ID
const length = 12; // Fixed spelling mistake
const upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const lowerCase = "abcdefghijklmnopqrstuvwxyz";
const number = "0123456789";
const symbol = "!@#$%^&*()_+-=[]{}|;:',.<>?/`~";
const allChars = upperCase + lowerCase + number + symbol;

function createPassword() {
    let password = "";

    // Ensuring at least one character from each category
    password += upperCase[Math.floor(Math.random() * upperCase.length)];
    password += lowerCase[Math.floor(Math.random() * lowerCase.length)];
    password += number[Math.floor(Math.random() * number.length)];
    password += symbol[Math.floor(Math.random() * symbol.length)];

    // Fill the remaining length
    while (password.length < length) {
        password += allChars[Math.floor(Math.random() * allChars.length)];
    }

    // Shuffle the password to randomize character positions
    password = password.split("").sort(() => Math.random() - 0.5).join("");

    // Assign the password to the input field
    passwordBox.value = password;
}

// Function to copy password
function copyPassword() {
    passwordBox.select();
    navigator.clipboard.writeText(passwordBox.value).then(() => {
        alert("Password copied to clipboard!");
    }).catch(err => {
        console.error("Failed to copy password: ", err);
    });
}
