let pass_btn = document.getElementById("password_btn")
pass_btn.addEventListener("click", generatePassword)

function generatePassword() {
    let password1Field = document.getElementById('id_password1');
    let password2Field = document.getElementById('id_password2');

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