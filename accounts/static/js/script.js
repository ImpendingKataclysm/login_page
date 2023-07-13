const pass_btn = document.getElementById("password_btn")
pass_btn.addEventListener("click", generatePassword)

/** Generates a secure password when the user requests one through the form,
 * and populates the password fields with the new password. */
function generatePassword() {
    const password1Field = document.getElementById('id_password1');
    const password2Field = document.getElementById('id_password2');

    password1Field.value = ''
    password2Field.value = ''

    let xhr = new XMLHttpRequest();
    xhr.open('GET', '/signup/', true);

    xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');

    xhr.onload = function() {
        if (xhr.status === 200) {
            let response = JSON.parse(xhr.responseText)
            let generatedPassword = response.password;
            password1Field.value = generatedPassword;
            password2Field.value = generatedPassword;
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