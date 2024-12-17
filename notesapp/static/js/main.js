const liked = document.getElementById('liked')
const unliked = document.getElementById('unliked')


unliked.addEventListener('click', () => {
    unliked.style.display = 'none';
    liked.style.display = 'block';
});
liked.addEventListener('click', () => {
    liked.style.display = 'none';
    unliked.style.display = 'block';
});