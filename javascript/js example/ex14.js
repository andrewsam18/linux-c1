var nameError = document.getElementById('name-error');
var phoneError = document.getElementById('phone-error');
var emailError = document.getElementById('email-error');
var messageError = document.getElementById('message-error');
var submitError = document.getElementById('submit-error');

function validateName() {
    var name = document.getElementById('contact-name').value.trim(); // Corrected `Value` to `value`
    
    if (name.length == 0) {
        nameError.innerHTML = 'Name is required';
        nameError.style.color = 'red';
        return false;
    }
    
    if (!name.match(/^[A-Za-z]+(\s[A-Za-z]+)+$/)) { // Allows multiple words
        nameError.innerHTML = 'Write full name (first and last)';
        nameError.style.color = 'red';
        return false;
    }
    
    nameError.innerHTML = '<i class="fas fa-check-circle"></i>';
    return true;
}

function validatePhone() {
    var phone = document.getElementById('contact-phone').value.trim();
    
    if (phone.length == 0) {
        phoneError.innerHTML = 'Phone number is required';
        phoneError.style.color = 'red';
        return false;
    }
    
    if (phone.length !== 10) {
        phoneError.innerHTML = 'Phone number should be 10 digits';
        phoneError.style.color = 'red';
        return false;
    }
    
    if (!phone.match(/^[0-9]{10}$/)) {
        phoneError.innerHTML = 'Only digits allowed';
        phoneError.style.color = 'red';
        return false;
    }
    
    phoneError.innerHTML = '<i class="fas fa-check-circle"></i>';
    return true;
}

function validateEmail() {
    var email = document.getElementById('contact-email').value.trim();
    
    if (email.length == 0) {
        emailError.innerHTML = 'Email is required';
        emailError.style.color = 'red';
        return false;
    }
    
    var emailPattern = /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/;
    if (!email.match(emailPattern)) {
        emailError.innerHTML = 'Invalid email format';
        emailError.style.color = 'red';
        return false;
    }
    
    emailError.innerHTML = '<i class="fas fa-check-circle"></i>';
    return true;
}

function validateMessage() {
    var message = document.getElementById('contact-message').value.trim();
    var required = 30;
    var left = required - message.length;

    if (left > 0) {
        messageError.innerHTML = left + ' more characters required';
        messageError.style.color = 'red';
        return false;
    }

    messageError.innerHTML = '<i class="fas fa-check-circle"></i>';
    return true;
}

function validateForm() {
    if (!validateName() || !validatePhone() || !validateEmail() || !validateMessage()) { // Fixed `validateMessage`
        submitError.style.display = 'block';
        submitError.innerHTML = 'Please fix errors before submitting';
        submitError.style.color = 'red';
        
        setTimeout(function () {
            submitError.style.display = 'none';
        }, 3000);
        
        return false;
    }
    
    submitError.innerHTML = '<i class="fas fa-check-circle"></i>';
    return true;
}
