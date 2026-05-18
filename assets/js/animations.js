document.addEventListener("DOMContentLoaded", () => {

  // --- INTERSECTION OBSERVER FOR SCROLL ANIMATIONS ---
  const observerOptions = {
    root: null,
    rootMargin: '0px 0px 150px 0px',
    threshold: 0.02
  };

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        
        // General reveals
        if (entry.target.classList.contains('reveal') || 
            entry.target.classList.contains('reveal-left') || 
            entry.target.classList.contains('reveal-right')) {
          entry.target.classList.add('active');
        }

        // Timeline drawing
        if (entry.target.classList.contains('timeline')) {
          entry.target.classList.add('active');
          const items = entry.target.querySelectorAll('.timeline-item');
          items.forEach((item, index) => {
            setTimeout(() => {
              item.classList.add('active');
            }, 120 * (index + 1)); // Stagger timeline items quickly
          });
        }

        // Progress bars
        if (entry.target.classList.contains('progress-bg')) {
          const fill = entry.target.querySelector('.progress-fill');
          if (fill) {
            const width = fill.getAttribute('data-width');
            fill.style.width = width;
          }
        }

        // Animated Numbers
        if (entry.target.classList.contains('stat-count') && !entry.target.classList.contains('counted')) {
          entry.target.classList.add('counted');
          const target = +entry.target.getAttribute('data-target');
          const duration = 1500; // ms
          const start = performance.now();
          
          const updateCount = (time) => {
            const progress = (time - start) / duration;
            if (progress < 1) {
              entry.target.innerText = Math.floor(progress * target) + (entry.target.getAttribute('data-suffix') || '');
              requestAnimationFrame(updateCount);
            } else {
              entry.target.innerText = target + (entry.target.getAttribute('data-suffix') || '');
            }
          };
          requestAnimationFrame(updateCount);
        }
        
        obs.unobserve(entry.target);
      }
    });
  }, observerOptions);

  // Select elements to observe
  const elementsToAnimate = document.querySelectorAll(
    '.reveal, .reveal-left, .reveal-right, .timeline, .progress-bg, .stat-count'
  );
  elementsToAnimate.forEach(el => observer.observe(el));


  // --- TYPING EFFECT ---
  const typeTarget = document.getElementById("typing-text");
  if (typeTarget) {
    const roles = ["Data Analyst", "Business Analyst", "AI Explorer"];
    let roleIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    let typingSpeed = 100;
    
    function typeEffect() {
      const currentRole = roles[roleIndex];
      
      if (isDeleting) {
        typeTarget.innerHTML = currentRole.substring(0, charIndex - 1);
        charIndex--;
        typingSpeed = 50;
      } else {
        typeTarget.innerHTML = currentRole.substring(0, charIndex + 1);
        charIndex++;
        typingSpeed = 100;
      }
      
      if (!isDeleting && charIndex === currentRole.length) {
        typingSpeed = 1500; // Pause at the end of word
        isDeleting = true;
      } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        roleIndex = (roleIndex + 1) % roles.length;
        typingSpeed = 500; // Pause before typing next word
      }
      
      setTimeout(typeEffect, typingSpeed);
    }
    
    setTimeout(typeEffect, 1000);
  }

  // --- DASHBOARD SLIDER ---
  const sliderTrack = document.getElementById('slider-track');
  if (sliderTrack) {
    const slides = document.querySelectorAll('.slide');
    const dotsContainer = document.getElementById('slider-dots');
    const btnPrev = document.getElementById('btn-prev');
    const btnNext = document.getElementById('btn-next');
    let currentIndex = 0;
    const totalSlides = slides.length;

    // Create dots
    for(let i=0; i<totalSlides; i++) {
        const dot = document.createElement('div');
        dot.classList.add('dot');
        if(i===0) dot.classList.add('active');
        dot.addEventListener('click', () => goToSlide(i));
        dotsContainer.appendChild(dot);
    }
    const dots = document.querySelectorAll('.dot');

    function updateSlider() {
        sliderTrack.style.transform = `translateX(-${currentIndex * 100}%)`;
        dots.forEach((dot, index) => {
            dot.classList.toggle('active', index === currentIndex);
        });
    }

    function goToSlide(index) {
        currentIndex = index;
        updateSlider();
    }

    if(btnNext) {
        btnNext.addEventListener('click', () => {
            currentIndex = (currentIndex + 1) % totalSlides;
            updateSlider();
        });
    }

    if(btnPrev) {
        btnPrev.addEventListener('click', () => {
            currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
            updateSlider();
        });
    }

    // Touch support (swipe)
    let startX = 0;
    let endX = 0;
    sliderTrack.addEventListener('touchstart', e => { startX = e.touches[0].clientX; });
    sliderTrack.addEventListener('touchend', e => {
        endX = e.changedTouches[0].clientX;
        if(startX - endX > 50) { // swipe left (next)
            currentIndex = (currentIndex + 1) % totalSlides;
            updateSlider();
        } else if(endX - startX > 50) { // swipe right (prev)
            currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
            updateSlider();
        }
    });
  }

  // --- BLOG MODAL EVENT LISTENERS ---
  const modal = document.getElementById('blog-modal');
  const closeBtn = document.getElementById('modal-close-btn');

  if (modal && closeBtn) {
      closeBtn.addEventListener('click', () => {
          modal.classList.remove('active');
          document.body.style.overflow = '';
      });

      // Click outside to close
      modal.addEventListener('click', (e) => {
          if (e.target === modal) {
              modal.classList.remove('active');
              document.body.style.overflow = '';
          }
      });
  }

});

// --- BLOG MODAL GLOBAL OPEN FUNCTION ---
window.openModal = function(contentId) {
  const modal = document.getElementById('blog-modal');
  const source = document.getElementById(contentId);
  if(!modal || !source) return;

  // Extract from hidden content
  const cat = source.querySelector('.meta-cat').innerText;
  const title = source.querySelector('.meta-title').innerText;
  const info = source.querySelector('.meta-info').innerHTML;
  const body = source.querySelector('.meta-body').innerHTML;

  // Inject into modal
  document.getElementById('modal-cat').innerText = cat;
  document.getElementById('modal-title').innerText = title;
  document.getElementById('modal-meta-info').innerHTML = info;
  document.getElementById('modal-body').innerHTML = body;

  // Show modal
  modal.classList.add('active');
  document.body.style.overflow = 'hidden'; // prevent bg scroll
};
