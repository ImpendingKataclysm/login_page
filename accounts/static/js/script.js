const pass_btn = document.getElementById("password_btn")
pass_btn.addEventListener("click", generatePassword)

/** Generates a secure password when the user requests one through the form,
 * and populates the password fields with the new password. */
function generatePassword() {
    let password1Field = document.getElementById('id_password1');
    let password2Field = document.getElementById('id_password2');

    if (password1Field === null && password2Field === null) {
        password1Field = document.getElementById('id_new_password1');
        password2Field = document.getElementById('id_new_password2');
    }

    password1Field.value = ''
    password2Field.value = ''

    getSecurePassword(password1Field, password2Field)
}

/**
 * Sends GET request to the Django backend for the generated password. If the
 * request is successful, the specified form fields are populated with the
 * retrieved password.
 * */
function getSecurePassword(field1, field2) {
    let xhr = new XMLHttpRequest();
    xhr.open('GET', '/signup/', true);

    xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');

    xhr.onload = function() {
        if (xhr.status === 200) {
            let response = JSON.parse(xhr.responseText)
            let generatedPassword = response.password;
            field1.value = generatedPassword;
            field2.value = generatedPassword;
        }
    };

    xhr.send()
}

const toggleBtn = document.getElementById("toggle_password")
let passwordFields = document.querySelectorAll('input[type="password"]');
toggleBtn.addEventListener("click", togglePasswordVisibility)

/** Change the current visibility of the text in the password fields */
function togglePasswordVisibility() {
    passwordFields.forEach(field => {
       if (field.type === 'password') {
           field.type = 'text';
       } else {
           field.type = 'password';
       }
    });
}