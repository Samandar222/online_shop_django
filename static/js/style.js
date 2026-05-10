const container = document.getElementById('container');

const registerTrigger = document.querySelector('.register-trigger');
const loginTrigger = document.querySelector('.login-trigger');

registerTrigger.addEventListener('click', (e) => {
    e.preventDefault();
    container.classList.add("toggled");
});

loginTrigger.addEventListener('click', (e) => {
    e.preventDefault();
    container.classList.remove("toggled");
});