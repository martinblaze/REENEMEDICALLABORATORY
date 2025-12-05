// Dark Mode Toggle
const darkModeToggle = document.getElementById('darkModeToggle');
const body = document.body;

// Check for saved user preference, if any, on load
const currentTheme = localStorage.getItem('theme') || 'light';
body.setAttribute('data-theme', currentTheme);

if (darkModeToggle) {
    // Update toggle button state
    if (currentTheme === 'dark') {
        darkModeToggle.innerHTML = '☀️';
        darkModeToggle.setAttribute('aria-label', 'Switch to light mode');
    }

    darkModeToggle.addEventListener('click', () => {
        let theme = body.getAttribute('data-theme');

        if (theme === 'light') {
            body.setAttribute('data-theme', 'dark');
            localStorage.setItem('theme', 'dark');
            darkModeToggle.innerHTML = '☀️';
            darkModeToggle.setAttribute('aria-label', 'Switch to light mode');
        } else {
            body.setAttribute('data-theme', 'light');
            localStorage.setItem('theme', 'light');
            darkModeToggle.innerHTML = '🌙';
            darkModeToggle.setAttribute('aria-label', 'Switch to dark mode');
        }
    });
}

// Mobile Navigation Toggle
const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('navLinks');

if (hamburger && navLinks) {
    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        navLinks.classList.toggle('active');
    });

    // Close menu when clicking on a link
    document.querySelectorAll('.nav-links a').forEach(link => {
        link.addEventListener('click', () => {
            hamburger.classList.remove('active');
            navLinks.classList.remove('active');
        });
    });

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!hamburger.contains(e.target) && !navLinks.contains(e.target)) {
            hamburger.classList.remove('active');
            navLinks.classList.remove('active');
        }
    });
}

// Contact Form Handler (for contact.html)
const contactForm = document.getElementById('contactForm');
if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
        e.preventDefault();

        const alertBox = document.getElementById('alertBox');
        const name = document.getElementById('name').value;
        const phone = document.getElementById('phone').value;
        const email = document.getElementById('email').value;
        const service = document.getElementById('service').value;
        const message = document.getElementById('message').value;

        const subject = encodeURIComponent('New Contact Form Submission - REENE Medical');
        const body = encodeURIComponent(
            `Name: ${name}\n` +
            `Phone: ${phone}\n` +
            `Email: ${email}\n` +
            `Service of Interest: ${service}\n\n` +
            `Message:\n${message}`
        );

        const mailtoLink = `mailto:info@reenemedicaldiagnostics.com?subject=${subject}&body=${body}`;

        window.location.href = mailtoLink;

        if (alertBox) {
            alertBox.className = 'alert alert-success';
            alertBox.style.display = 'block';
            alertBox.textContent = 'Opening your email client... Please send the message to complete your inquiry.';

            setTimeout(() => {
                this.reset();
                alertBox.style.display = 'none';
            }, 3000);
        }
    });
}