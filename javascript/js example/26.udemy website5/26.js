// Wait until the DOM is fully loaded
document.addEventListener("DOMContentLoaded", function () {
    // Navbar toggle (Bootstrap handles this by default, but adding animation logic if needed)
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('#navbarNav');

    if (navbarToggler) {
        navbarToggler.addEventListener('click', function () {
            navbarCollapse.classList.toggle('show');
        });
    }

    // Smooth scrolling for internal links
    const links = document.querySelectorAll('a[href^="#"]');
    links.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Highlight active nav item on scroll (basic example)
    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');

    window.addEventListener('scroll', function () {
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 80;
            if (pageYOffset >= sectionTop) {
                current = section.getAttribute('class');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active-home');
            if (link.getAttribute('href').includes(current)) {
                link.classList.add('active-home');
            }
        });
    });

    // Carousel fallback control (if needed)
    if (typeof $ !== 'undefined' && typeof $.fn.carousel !== 'undefined') {
        $('#carouselExampleCaptions').carousel({
            interval: 5000
        });
    }

    // Newsletter form validation (basic)
    const form = document.querySelector("form");
    const emailInput = form.querySelector('input[type="email"]');

    form.addEventListener("submit", function (e) {
        const emailValue = emailInput.value.trim();
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if (!emailRegex.test(emailValue)) {
            e.preventDefault();
            alert("Please enter a valid email address.");
        }
    });
});
