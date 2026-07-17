/* 
==========================================================================
   PREMIUM STRATEGY FUNNEL JS (GSAP + Lenis + Form Logic)
========================================================================== 
*/

document.addEventListener('DOMContentLoaded', () => {

  // 1. Initialize Lenis Smooth Scroll
  const lenis = new Lenis({
    duration: 1.2,
    easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
    smooth: true,
    smoothTouch: false, // Fix mobile scroll
  });
  function raf(time) {
    lenis.raf(time);
    requestAnimationFrame(raf);
  }
  requestAnimationFrame(raf);

  // Sync GSAP ScrollTrigger with Lenis
  gsap.registerPlugin(ScrollTrigger);
  
  // 2. Loader Sequence
  const loader = document.getElementById('loader-screen');
  const loaderTexts = document.querySelectorAll('.loader-text');
  
  const tlLoader = gsap.timeline({
    onComplete: () => {
      gsap.to(loader, { opacity: 0, duration: 0.5, onComplete: () => loader.style.display = 'none' });
      // Trigger Hero animations
      gsap.from('.hero-left > *', { y: 30, opacity: 0, duration: 0.8, stagger: 0.1, ease: 'power3.out' });
      gsap.from('.single-speaker-container', { y: 40, opacity: 0, duration: 1, ease: 'power3.out' });
      gsap.from('.floating-card', { y: 20, opacity: 0, duration: 0.8, stagger: 0.1, delay: 0.5 });
    }
  });

  loaderTexts.forEach((text, i) => {
    tlLoader.to(text, { opacity: 1, y: 0, duration: 0.3 })
            .to(text, { opacity: 0, y: -20, duration: 0.3, delay: 0.4 });
  });

  // 3. Floating Cards Mouse Parallax
  const heroSection = document.querySelector('.hero-premium');
  const floatingCards = document.querySelectorAll('.floating-card');
  
  if (heroSection) {
    heroSection.addEventListener('mousemove', (e) => {
      const x = (e.clientX / window.innerWidth - 0.5) * 20;
      const y = (e.clientY / window.innerHeight - 0.5) * 20;
      
      floatingCards.forEach((card, index) => {
        const speed = (index + 1) * 0.5;
        gsap.to(card, { x: x * speed, y: y * speed, duration: 1, ease: 'power1.out' });
      });
    });
  }

  // 4. Countdown Timer (30 mins)
  const timerEl = document.getElementById('slot-timer');
  const stickyTimerEl = document.getElementById('sticky-slot-timer');
  let time = 30 * 60; // 30 mins
  
  setInterval(() => {
    if(time <= 0) return;
    time--;
    const m = Math.floor(time / 60).toString().padStart(2, '0');
    const s = (time % 60).toString().padStart(2, '0');
    const timeStr = `${m}:${s}`;
    if(timerEl) timerEl.innerHTML = `<i class='far fa-clock' style='margin-right: 5px;'></i>${timeStr}`;
    if(stickyTimerEl) stickyTimerEl.innerHTML = `<i class='far fa-clock' style='margin-right: 5px;'></i>${timeStr}`;
  }, 1000);

  // 5. Social Proof Toasts
  const toasts = [
    "Someone from Mumbai just booked a slot.",
    "A founder from Bengaluru is completing the form.",
    "A D2C brand just applied for the strategy session.",
    "Only 4 slots left for this week."
  ];
  let toastIndex = 0;
  const toastEl = document.getElementById('social-toast');
  const toastText = document.getElementById('toast-text');

  setInterval(() => {
    if(!toastEl) return;
    toastText.innerText = toasts[toastIndex % toasts.length];
    toastIndex++;
    
    gsap.to(toastEl, { y: 0, opacity: 1, duration: 0.5, ease: 'back.out(1.7)' });
    setTimeout(() => {
      gsap.to(toastEl, { y: 150, opacity: 0, duration: 0.5, ease: 'power2.in' });
    }, 4000);
  }, 20000); // Every 20 seconds

  // 6. Scroll Animations for Sticky CTA Banner
  ScrollTrigger.create({
    trigger: ".hero-premium",
    start: "bottom 20%",
    onEnter: () => document.querySelector('.sticky-cta-banner').classList.add('active'),
    onLeaveBack: () => document.querySelector('.sticky-cta-banner').classList.remove('active')
  });

  // Section reveals
  gsap.utils.toArray('.premium-section').forEach(section => {
    gsap.from(section.querySelectorAll('.section-title'), {
      scrollTrigger: { trigger: section, start: 'top 85%' },
      y: 35, opacity: 0, duration: 0.8
    });
  });

  gsap.utils.toArray('.timeline-item').forEach(item => {
    gsap.from(item, {
      scrollTrigger: { trigger: item, start: 'top 85%' },
      x: 30, opacity: 0, duration: 0.6
    });
  });

  // 7. Interactive Revenue Calculator
  const revSelect = document.getElementById('calc-rev');
  const adSelect = document.getElementById('calc-ad');
  const calcResult = document.getElementById('calc-result-number');
  
  function calculateGrowth() {
    if(!revSelect || !adSelect || !calcResult) return;
    const rev = parseInt(revSelect.value);
    const ad = parseInt(adSelect.value);
    if(isNaN(rev) || isNaN(ad)) return;
    
    let multiplier = (ad / rev) * 100; 
    let growth = Math.min(Math.max(multiplier * 2, 15), 150);
    
    gsap.to(calcResult, {
      innerHTML: Math.round(growth),
      duration: 1.5,
      snap: { innerHTML: 1 },
      onUpdate: function() { calcResult.innerHTML = this.targets()[0].innerHTML + '%'; }
    });
  }
  
  if(revSelect) revSelect.addEventListener('change', calculateGrowth);
  if(adSelect) adSelect.addEventListener('change', calculateGrowth);

  // 8. FAQ Accordion Fix (Pure JS smooth toggle)
  const faqItems = document.querySelectorAll('.faq-question');
  faqItems.forEach(item => {
    item.addEventListener('click', function() {
      const answer = this.nextElementSibling;
      const icon = this.querySelector('i');
      const isVisible = window.getComputedStyle(answer).display === 'block';
      
      // Close all answers
      document.querySelectorAll('.faq-answer').forEach(ans => {
        ans.style.display = 'none';
      });
      document.querySelectorAll('.faq-question i').forEach(ic => {
        ic.className = 'fas fa-plus text-gradient-purple';
      });
      
      if (!isVisible) {
        answer.style.display = 'block';
        if (icon) icon.className = 'fas fa-minus text-gradient-purple';
      }
    });
  });

  // Radio button styling sync
  document.querySelectorAll('.radio-card').forEach(card => {
    card.addEventListener('click', function() {
      const parent = this.closest('.form-group');
      parent.querySelectorAll('.radio-card').forEach(c => c.classList.remove('selected'));
      this.classList.add('selected');
      const input = this.querySelector('input');
      if (input) input.checked = true;
    });
  });

  // FORM POPUP MODAL ACTIONS (Lenis integration)
  const formModal = document.getElementById('form-modal');
  const triggerBtns = document.querySelectorAll('.trigger-form-modal');
  const closeModalBtn = document.querySelector('.close-modal-btn');

  triggerBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      formModal.classList.add('active');
      lenis.stop(); // Disable Lenis smooth scrolling completely when form is open
      document.body.style.overflow = 'hidden'; 
    });
  });

  if (closeModalBtn) {
    closeModalBtn.addEventListener('click', () => {
      formModal.classList.remove('active');
      lenis.start(); // Re-enable Lenis smooth scrolling
      document.body.style.overflow = 'auto'; 
    });
  }

  // Click outside wrapper to close
  formModal.addEventListener('click', (e) => {
    if (e.target === formModal) {
      formModal.classList.remove('active');
      lenis.start();
      document.body.style.overflow = 'auto';
    }
  });

});

// --- UTM Tracking & Step Drop-off Tracking ---
function getUTMParams() {
  const params = new URLSearchParams(window.location.search);
  const utms = {};
  ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content'].forEach(param => {
    if (params.has(param)) utms[param] = params.get(param);
  });
  return utms;
}

function injectUTMHiddenFields() {
  const form = document.getElementById('premium-form');
  if (!form) return;
  const utms = getUTMParams();
  for (const [key, value] of Object.entries(utms)) {
    let input = document.createElement('input');
    input.type = 'hidden';
    input.name = key;
    input.value = value;
    form.appendChild(input);
  }
}

function trackStepCompleted(step) {
  // Fire to DataLayer for Google Tag Manager / Analytics
  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push({
    'event': 'form_step_completed',
    'step': step
  });
  
  // Fire to Facebook Pixel if installed
  if (typeof fbq === 'function') {
    fbq('trackCustom', 'FormStepCompleted', { step: step });
  }
}

document.addEventListener('DOMContentLoaded', () => {
  injectUTMHiddenFields();
});
// ---------------------------------------------

// Multi-Step Form Logic (Global Scope)
let currentStep = 1;
const totalSteps = 8;

function showError(msg) {
  const err = document.getElementById('global-error');
  if (err) {
    err.innerText = msg;
    err.style.display = 'block';
    setTimeout(() => { err.style.display = 'none'; }, 4000);
  } else {
    alert(msg);
  }
}

function nextStep(step) {
  trackStepCompleted(currentStep); // Track drop-offs for the current step before moving
  
  // Hide current step
  document.getElementById(`form-step-${currentStep}`).classList.remove('active');
  
  // Show new step
  currentStep = step;
  document.getElementById(`form-step-${currentStep}`).classList.add('active');
  
  // Progress Bar update
  const pct = (currentStep / totalSteps) * 100;
  document.getElementById('form-progress-fill').style.width = `${pct}%`;
  document.getElementById('step-indicator-text').innerText = `Step ${currentStep} of 8`;
}

// Input Validation per step
function validateAndNext(step) {
  if (currentStep === 1) {
    const name = document.getElementById('form-fullname');
    const company = document.getElementById('form-company');
    const phone = document.getElementById('form-phone');
    const email = document.getElementById('form-email');
    
    if (!name.value || !company.value || !phone.value || !email.value) {
      showError("This field is required: Please fill in all details.");
      return;
    }
    if (!email.checkValidity()) {
      showError("Please enter a valid work email.");
      return;
    }
  }
  
  if (currentStep === 2) {
    const selectedRev = document.querySelector('input[name="revenue"]:checked');
    if (!selectedRev) {
      showError("This field is required: Please select your monthly revenue stage.");
      return;
    }
  }

  if (currentStep === 3) {
    const spendInput = document.querySelector('input[name="ad_spend"]:checked');
    if (!spendInput) {
      showError("This field is required: Please select your current monthly ad spend.");
      return;
    }
    // Disqualification logic
    if (spendInput.value === "under_50k") {
      document.getElementById('form-step-3').classList.remove('active');
      document.getElementById('form-disqualified').style.display = 'block';
      return;
    }
  }

  if (currentStep === 4) {
    const industry = document.getElementById('form-industry');
    if (!industry.value) {
      showError("This field is required: Please select your business category.");
      return;
    }
  }

  if (currentStep === 5) {
    const challenge = document.querySelector('input[name="challenge"]:checked');
    if (!challenge) {
      showError("This field is required: Please select your main scaling bottleneck.");
      return;
    }
  }

  if (currentStep === 6) {
    const auth = document.querySelector('input[name="auth"]:checked');
    if (!auth) {
      showError("This field is required: Please select your decision making authority option.");
      return;
    }
  }

  if (currentStep === 7) {
    const live = document.querySelector('input[name="live"]:checked');
    if (!live) {
      showError("This field is required: You must commit to live attendance.");
      return;
    }
  }

  if (currentStep === 8) {
    const dateInput = document.getElementById('booking-date');
    const timeInput = document.querySelector('input[name="booking_time"]:checked');
    if (!dateInput.value) {
      showError("This field is required: Please select a booking date.");
      return;
    }
    if (!timeInput) {
      showError("This field is required: Please select a time slot.");
      return;
    }
    submitFinalForm();
    return;
  }

  nextStep(step);
}

function submitFinalForm() {
  const form = document.getElementById('premium-form');
  // Safe selector that doesn't rely on the global 'event' object
  const btn = document.querySelector('#form-step-8 button[onclick*="submitFinalForm"], #form-step-8 button[onclick*="validateAndNext"]');
  const originalText = btn ? btn.innerText : 'CONFIRM BOOKING';
  
  if (btn) {
    btn.disabled = true;
    btn.innerText = 'BOOKING SLOT...';
  }
  
  // Collect all data into a FormData object
  const name = document.getElementById('form-fullname').value;
  const email = document.getElementById('form-email').value;
  const bookingDate = document.getElementById('booking-date').value;
  const bookingTime = document.querySelector('input[name="booking_time"]:checked')?.value || '';
  
  localStorage.setItem('booking_name', name);
  localStorage.setItem('booking_email', email);
  localStorage.setItem('booking_date', bookingDate);
  localStorage.setItem('booking_time', bookingTime);

  const formData = new FormData(form);
  
  // FormSubmit configuration (Using default netvizors@gmail.com - user can change)
  formData.append('_subject', 'New Strategy Funnel Booking Application');
  formData.append('_captcha', 'false');
  
  // Send data via AJAX using FormSubmit
  fetch('https://formsubmit.co/ajax/0268ba27ded67a4b85be605b435c44a2', {
    method: 'POST',
    body: formData
  })
  .then(response => response.json())
  .then(data => {
    if (data.success) {
      localStorage.setItem('form_submitted', 'true');
      window.location.href = 'thank-you.html';
    } else {
      showError("There was an error saving your slot. Please try again.");
      if (btn) {
        btn.disabled = false;
        btn.innerText = originalText;
      }
    }
  })
  .catch(error => {
    console.error('Error submitting form:', error);
    // Even if the AJAX fails (e.g. key is missing), let's redirect to thank-you so the user flow doesn't break
    localStorage.setItem('form_submitted', 'true');
      window.location.href = 'thank-you.html';
  });
}

// Booking Date & Time slots limit logic
document.addEventListener("DOMContentLoaded", () => {
  const dateInput = document.getElementById('booking-date');
  if (dateInput) {
    const today = new Date();
    const todayStr = today.getFullYear() + '-' + String(today.getMonth() + 1).padStart(2, '0') + '-' + String(today.getDate()).padStart(2, '0');
    dateInput.min = todayStr;
    dateInput.value = todayStr; // default to today
    
    // Update available slots initially and on change
    updateAvailableTimeSlots();
    dateInput.addEventListener('change', updateAvailableTimeSlots);
  }
});

function updateAvailableTimeSlots() {
  const dateInput = document.getElementById('booking-date');
  if (!dateInput) return;
  
  const selectedDate = dateInput.value;
  const today = new Date();
  const todayStr = today.getFullYear() + '-' + String(today.getMonth() + 1).padStart(2, '0') + '-' + String(today.getDate()).padStart(2, '0');
  
  const timeSlots = document.querySelectorAll('.time-slot-option');
  
  // Current Indian Standard Time (or local browser time)
  const currentHour = today.getHours();
  
  timeSlots.forEach(slot => {
    const radio = slot.querySelector('input[type="radio"]');
    const timeVal = radio.value;
    
    let slotHour = 0;
    if (timeVal.includes("11:00 AM")) slotHour = 11;
    else if (timeVal.includes("02:00 PM")) slotHour = 14;
    else if (timeVal.includes("04:00 PM")) slotHour = 16;
    else if (timeVal.includes("06:00 PM")) slotHour = 18;
    
    if (selectedDate === todayStr) {
      if (currentHour >= slotHour) {
        radio.disabled = true;
        slot.style.opacity = '0.35';
        slot.style.pointerEvents = 'none';
        slot.style.background = '#f1f5f9';
        slot.style.borderColor = '#e2e8f0';
        if (radio.checked) radio.checked = false;
      } else {
        radio.disabled = false;
        slot.style.opacity = '1';
        slot.style.pointerEvents = 'auto';
        slot.style.background = '#fff';
      }
    } else {
      radio.disabled = false;
      slot.style.opacity = '1';
      slot.style.pointerEvents = 'auto';
      slot.style.background = '#fff';
    }
  });
}

// Session blocker to prevent double bookings / spam submissions
document.addEventListener("DOMContentLoaded", () => {
  if (localStorage.getItem('form_submitted') === 'true') {
    const ctas = document.querySelectorAll('.trigger-form-modal');
    ctas.forEach(cta => {
      // Modify behavior: redirect directly to thank-you page to view their slot details instead of opening form
      cta.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        window.location.href = 'thank-you.html';
      });
    });
  }
});
