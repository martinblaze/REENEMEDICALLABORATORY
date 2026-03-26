// ── Dark Mode ──
const darkModeToggle = document.getElementById('darkModeToggle');
const body = document.body;

if (darkModeToggle) {
  const saved = localStorage.getItem('theme') || 'light';
  body.setAttribute('data-theme', saved);
  darkModeToggle.innerHTML = saved === 'dark' ? '☀️' : '🌙';

  darkModeToggle.addEventListener('click', () => {
    const theme = body.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    body.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
    darkModeToggle.innerHTML = theme === 'dark' ? '☀️' : '🌙';
    darkModeToggle.setAttribute('aria-label', theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
  });
}

// ── Mobile Nav ──
const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('navLinks');

if (hamburger && navLinks) {
  hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    navLinks.classList.toggle('active');
    document.body.style.overflow = navLinks.classList.contains('active') ? 'hidden' : '';
  });

  document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => {
      hamburger.classList.remove('active');
      navLinks.classList.remove('active');
      document.body.style.overflow = '';
    });
  });

  document.addEventListener('click', (e) => {
    if (!hamburger.contains(e.target) && !navLinks.contains(e.target)) {
      hamburger.classList.remove('active');
      navLinks.classList.remove('active');
      document.body.style.overflow = '';
    }
  });
}

// ── Scroll Reveal ──
const reveals = document.querySelectorAll('.reveal');
if (reveals.length) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        const delay = entry.target.dataset.delay || 0;
        setTimeout(() => {
          entry.target.classList.add('visible');
        }, delay);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

  // Stagger cards in grids
  document.querySelectorAll('.services-grid .service-card, .features-grid .feature-box, .values-grid .value-card, .team-grid .team-member, .gallery-grid .gallery-item, .booking-methods .booking-card').forEach((el, i) => {
    el.dataset.delay = (i % 3) * 80;
  });

  reveals.forEach(el => observer.observe(el));
}

// ── Header scroll shadow ──
window.addEventListener('scroll', () => {
  const header = document.querySelector('header');
  if (header) {
    header.style.boxShadow = window.scrollY > 10
      ? '0 4px 24px rgba(0,0,0,0.35)'
      : '0 2px 20px rgba(0,0,0,0.25)';
  }
}, { passive: true });

// ── Contact Form ──
const contactForm = document.getElementById('contactForm');
if (contactForm) {
  contactForm.addEventListener('submit', function(e) {
    e.preventDefault();
    const alertBox = document.getElementById('alertBox');
    const name    = document.getElementById('name').value;
    const phone   = document.getElementById('phone').value;
    const email   = document.getElementById('email').value;
    const service = document.getElementById('service').value;
    const message = document.getElementById('message').value;

    const subject = encodeURIComponent('Appointment / Inquiry — Reene Medical Diagnostics');
    const bodyText = encodeURIComponent(
      `Name: ${name}\nPhone: ${phone}\nEmail: ${email}\nService: ${service}\n\nMessage:\n${message}`
    );

    window.location.href = `mailto:info@reenemedicaldiagnostics.com?subject=${subject}&body=${bodyText}`;

    if (alertBox) {
      alertBox.className = 'alert alert-success';
      alertBox.style.display = 'block';
      alertBox.textContent = 'Opening your email client... Please send the message to complete your inquiry.';
      setTimeout(() => {
        this.reset();
        alertBox.style.display = 'none';
      }, 4000);
    }
  });
}