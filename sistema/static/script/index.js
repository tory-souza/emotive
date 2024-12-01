const dots = document.querySelectorAll('.dot');
const slides = document.querySelectorAll('.slides img');
let currentSlide = 0;

function changeSlide(newIndex) {
    // Prevent index overflow
    if (newIndex < 0) newIndex = slides.length - 1;
    if (newIndex >= slides.length) newIndex = 0;

    // Update slide position
    const slidesContainer = document.querySelector('.slides');
    slidesContainer.style.transform = `translateX(-${newIndex * 100}%)`;

    // Update active dot
    dots.forEach(dot => dot.classList.remove('active'));
    dots[newIndex].classList.add('active');

    currentSlide = newIndex;
}

// Add event listeners for dot navigation
dots.forEach((dot, index) => {
    dot.addEventListener('click', () => changeSlide(index));
});

// Optional: Auto-slide every 3 seconds
setInterval(() => {
    changeSlide(currentSlide + 1);
}, 3000);

// Initialize first slide
changeSlide(0);
