document.addEventListener('DOMContentLoaded', () => {
    const authWrapper = document.querySelector('.auth-wrapper');
    const registerBtn = document.querySelector('.switch-link a'); // Sign Up linki

    if (registerBtn) {
        registerBtn.addEventListener('click', (e) => {
            // Agar faqat effekt bermoqchi bo'lsangiz:
            // e.preventDefault();
            authWrapper.style.transform = "scale(1.05)";
            setTimeout(() => {
                authWrapper.style.transform = "scale(1)";
            }, 300);
        });
    }
});