function checkPasswordMatch() {
	const password = document.getElementById('signupname').value;
	const confirm_password = document.getElementById('signupconfirm_password').value;
	const message = document.getElementById('password_match_message');

	if (password === confirm_password) {
		message.textContent = 'Password Match!';
		message.style.color = 'green';
		
	}
	else {
		message.textContent = 'Password do not match!';
		message.style.color = 'red';
	}
}

document.addEventListener('DOMContentLoaded', function () {
	const passwordInput = document.getElementById('signpassword');
	const confirmInput = document.getElementById('signupconfirm_password');

	passwordInput.addEventListener('input',checkPasswordMatch);
	confirmInput.addEventListener('input', checkPasswordMatch);
});
