document.addEventListener('DOMContentLoaded', () => {
  initNavbar();
  initScrollReveal();
  initCounters();
  initServicesTabs();
  initPortfolioFilter();
  initFaqAccordion();
  initAuditWizard();
  initCareersModal();
  initContactForm();
  initNewsletterForm();
  initMegaMenuTabs();
});

/* ==========================================================================
   1. Navigation & Header scrolled class
   ========================================================================== */
function initNavbar() {
  const header = document.querySelector('.header');
  const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
  const navLinks = document.querySelector('.nav-links');

  // Add background shadow on scroll
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  });

  // Mobile menu toggle
  if (mobileMenuBtn && navLinks) {
    mobileMenuBtn.addEventListener('click', () => {
      navLinks.classList.toggle('mobile-active');
      const isExpanded = navLinks.classList.contains('mobile-active');
      mobileMenuBtn.innerHTML = isExpanded ? '<i class="fas fa-times"></i>' : '<i class="fas fa-bars"></i>';
      if (isExpanded) {
        document.body.style.overflow = 'hidden';
      } else {
        document.body.style.overflow = '';
      }
    });

    // Handle link clicks (close menu unless it's a dropdown toggle)
    const links = navLinks.querySelectorAll('a');
    links.forEach(link => {
      link.addEventListener('click', (e) => {
        const parentLi = link.parentElement;
        if ((parentLi.classList.contains('dropdown') || parentLi.classList.contains('mega-dropdown')) && window.innerWidth <= 768) {
          e.preventDefault();
          parentLi.classList.toggle('active-dropdown');
          const dropdownContent = parentLi.querySelector('.dropdown-content') || parentLi.querySelector('.mega-menu-content');
          if (dropdownContent) {
            if (dropdownContent.style.display === 'flex' || dropdownContent.style.display === 'grid') {
              dropdownContent.style.display = 'none';
            } else {
              dropdownContent.style.display = parentLi.classList.contains('mega-dropdown') ? 'grid' : 'flex';
            }
          }
        } else {
          navLinks.classList.remove('mobile-active');
          mobileMenuBtn.innerHTML = '<i class="fas fa-bars"></i>';
          document.body.style.overflow = '';
        }
      });
    });
  }
}

function initMegaMenuTabs() {
  const megaTabs = document.querySelectorAll('.mega-tab-btn');
  megaTabs.forEach(tab => {
    const handleSwitch = (e) => {
      e.stopPropagation();
      const targetPaneId = tab.getAttribute('data-tab');
      const parentDropdown = tab.closest('.mega-dropdown');
      if (parentDropdown) {
        parentDropdown.querySelectorAll('.mega-tab-btn').forEach(btn => btn.classList.remove('active'));
        parentDropdown.querySelectorAll('.mega-menu-pane').forEach(pane => pane.classList.remove('active'));
        tab.classList.add('active');
        const targetPane = parentDropdown.querySelector(`#${targetPaneId}`);
        if (targetPane) {
          targetPane.classList.add('active');
        }
      }
    };
    // tab.addEventListener('mouseover', handleSwitch);
    tab.addEventListener('click', handleSwitch);
  });
}

/* ==========================================================================
   2. Scroll Reveal Animations
   ========================================================================== */
function initScrollReveal() {
  const revealElements = document.querySelectorAll('.reveal');
  
  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
        observer.unobserve(entry.target); // Reveal only once
      }
    });
  }, {
    threshold: 0.15,
    rootMargin: '0px 0px -50px 0px'
  });

  revealElements.forEach(el => {
    revealObserver.observe(el);
  });
}

/* ==========================================================================
   3. Animated Metrics Counters
   ========================================================================== */
function initCounters() {
  const counterElements = document.querySelectorAll('.counter');
  
  const counterObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateCounter(entry.target);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });

  counterElements.forEach(el => {
    counterObserver.observe(el);
  });

  function animateCounter(el) {
    const target = parseFloat(el.getAttribute('data-target'));
    const duration = 2000; // 2 seconds
    const startTime = performance.now();
    const isFloat = el.getAttribute('data-float') === 'true';
    const suffix = el.getAttribute('data-suffix') || '';

    function update(currentTime) {
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);
      
      // Ease out quad formula
      const easeProgress = progress * (2 - progress);
      const currentVal = easeProgress * target;

      if (isFloat) {
        el.textContent = currentVal.toFixed(1) + suffix;
      } else {
        el.textContent = Math.floor(currentVal).toLocaleString() + suffix;
      }

      if (progress < 1) {
        requestAnimationFrame(update);
      } else {
        if (isFloat) {
          el.textContent = target.toFixed(1) + suffix;
        } else {
          el.textContent = target.toLocaleString() + suffix;
        }
      }
    }
    
    requestAnimationFrame(update);
  }
}

/* ==========================================================================
   4. Services Interactive Tab Selector
   ========================================================================== */
function initServicesTabs() {
  const tabButtons = document.querySelectorAll('.service-tab-btn');
  const tabContents = document.querySelectorAll('.service-tab-content');

  if (tabButtons.length === 0) return;

  tabButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetId = btn.getAttribute('data-tab');
      
      // Deactivate all
      tabButtons.forEach(b => b.classList.remove('active'));
      tabContents.forEach(c => c.classList.remove('active'));
      
      // Activate target
      btn.classList.add('active');
      const targetContent = document.getElementById(targetId);
      if (targetContent) {
        targetContent.classList.add('active');
      }
    });
  });
}

/* ==========================================================================
   5. Portfolio Filtering Logic
   ========================================================================== */
function initPortfolioFilter() {
  const filterButtons = document.querySelectorAll('.filter-btn');
  const portfolioCards = document.querySelectorAll('.portfolio-card');

  if (filterButtons.length === 0) return;

  filterButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const filter = btn.getAttribute('data-filter');
      
      // Toggle button active classes
      filterButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      // Filter grid cards
      portfolioCards.forEach(card => {
        const category = card.getAttribute('data-category');
        
        if (filter === 'all' || category === filter) {
          card.style.display = 'block';
          // Smooth fade-in trigger
          setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'scale(1)';
          }, 10);
        } else {
          card.style.opacity = '0';
          card.style.transform = 'scale(0.9)';
          setTimeout(() => {
            card.style.display = 'none';
          }, 300);
        }
      });
    });
  });
}

/* ==========================================================================
   6. FAQ Accordion Logic
   ========================================================================== */
function initFaqAccordion() {
  const faqButtons = document.querySelectorAll('.faq-question-btn');

  if (faqButtons.length === 0) return;

  faqButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const item = btn.parentElement;
      const isActive = item.classList.contains('active');

      // Collapse all other items
      document.querySelectorAll('.faq-item').forEach(i => {
        if (i !== item) {
          i.classList.remove('active');
        }
      });

      // Toggle current item
      if (isActive) {
        item.classList.remove('active');
      } else {
        item.classList.add('active');
      }
    });
  });
}

/* ==========================================================================
   7. Free Growth Audit Multi-Step Wizard
   ========================================================================== */
function initAuditWizard() {
  const auditForm = document.getElementById('audit-wizard-form');
  if (!auditForm) return;

  const steps = auditForm.querySelectorAll('.audit-step');
  const progressSteps = document.querySelectorAll('.progressbar-step');
  const progressBarFill = document.querySelector('.audit-progress-fill');
  const btnPrev = document.getElementById('audit-prev-btn');
  const btnNext = document.getElementById('audit-next-btn');
  const auditSuccessPanel = document.querySelector('.audit-success');
  const auditFormControls = auditForm.querySelector('.audit-form-inner');

  let currentStepIndex = 0;
  updateStepView();

  // Choice Selection buttons within wizard steps
  const selectButtons = auditForm.querySelectorAll('.select-btn');
  selectButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetInputId = btn.getAttribute('data-input-id');
      const value = btn.getAttribute('data-val');
      const parentContainer = btn.parentElement;
      
      // Deactivate siblings
      parentContainer.querySelectorAll('.select-btn').forEach(b => b.classList.remove('active'));
      // Activate selected
      btn.classList.add('active');
      
      // Update hidden input field value
      const hiddenInput = document.getElementById(targetInputId);
      if (hiddenInput) {
        hiddenInput.value = value;
      }
    });
  });

  // Next step trigger
  btnNext.addEventListener('click', () => {
    if (validateStep(currentStepIndex)) {
      if (currentStepIndex < steps.length - 1) {
        currentStepIndex++;
        updateStepView();
      } else {
        submitAuditWizard();
      }
    }
  });

  // Previous step trigger
  btnPrev.addEventListener('click', () => {
    if (currentStepIndex > 0) {
      currentStepIndex--;
      updateStepView();
    }
  });

  function updateStepView() {
    // Toggle step classes
    steps.forEach((step, idx) => {
      step.classList.toggle('active', idx === currentStepIndex);
    });

    // Update progress steps visual
    progressSteps.forEach((step, idx) => {
      if (idx < currentStepIndex) {
        step.className = 'progressbar-step completed';
      } else if (idx === currentStepIndex) {
        step.className = 'progressbar-step active';
      } else {
        step.className = 'progressbar-step';
      }
    });

    // Update progress line length
    const fillPercent = (currentStepIndex / (steps.length - 1)) * 100;
    progressBarFill.style.width = fillPercent + '%';

    // Show/hide previous button
    btnPrev.style.display = currentStepIndex === 0 ? 'none' : 'block';
    
    // Change next button text on final step
    btnNext.textContent = currentStepIndex === steps.length - 1 ? 'Get My Free Plan' : 'Continue';
  }

  function validateStep(stepIdx) {
    const activeStep = steps[stepIdx];
    const inputs = activeStep.querySelectorAll('.form-control[required], input[type="hidden"][required]');
    let isValid = true;

    inputs.forEach(input => {
      // Clear previous error styles
      input.style.borderColor = '';
      
      if (!input.value.trim()) {
        isValid = false;
        input.style.borderColor = '#EF4444'; // Red alert border
      }
      
      // Specific email validation
      if (input.type === 'email' && input.value) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(input.value)) {
          isValid = false;
          input.style.borderColor = '#EF4444';
        }
      }
    });

    return isValid;
  }

  function submitAuditWizard() {
    // In a live app, you would send form data using fetch().
    // We simulate form submission and show success animation.
    auditFormControls.style.display = 'none';
    auditSuccessPanel.style.display = 'block';
  }
}

/* ==========================================================================
   8. Careers Application Modal
   ========================================================================== */
function initCareersModal() {
  const modalOverlay = document.getElementById('apply-modal');
  const closeBtn = document.getElementById('close-apply-modal');
  const openButtons = document.querySelectorAll('.apply-btn');
  const applicationForm = document.getElementById('career-apply-form');
  const jobTitleInput = document.getElementById('apply-job-title');
  const modalFormInner = document.getElementById('modal-form-inner');
  const modalSuccess = document.getElementById('modal-success-screen');

  if (!modalOverlay) return;

  openButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const jobTitle = btn.getAttribute('data-job') || 'Growth Strategy Role';
      
      if (jobTitleInput) {
        jobTitleInput.value = jobTitle;
      }
      
      modalOverlay.classList.add('active');
      document.body.style.overflow = 'hidden'; // Lock background scroll
    });
  });

  function closeModal() {
    modalOverlay.classList.remove('active');
    document.body.style.overflow = '';
    
    // Reset modal states
    if (applicationForm) applicationForm.reset();
    if (modalFormInner) modalFormInner.style.display = 'block';
    if (modalSuccess) modalSuccess.style.display = 'none';
  }

  closeBtn.addEventListener('click', closeModal);
  modalOverlay.addEventListener('click', (e) => {
    if (e.target === modalOverlay) closeModal();
  });

  if (applicationForm) {
    applicationForm.addEventListener('submit', (e) => {
      e.preventDefault();
      
      const formData = new FormData(applicationForm);
      const submitBtn = applicationForm.querySelector('button[type="submit"]');
      const originalText = submitBtn ? submitBtn.innerText : 'Submit Application';
      
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerText = 'Sending...';
      }

      fetch('https://formsubmit.co/ajax/nasrinjariwala176@gmail.com', {
        method: 'POST',
        body: formData
      })
      .then(response => response.json())
      .then(data => {
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerText = originalText;
        }
        if (modalFormInner) modalFormInner.style.display = 'none';
        if (modalSuccess) modalSuccess.style.display = 'block';
      })
      .catch(error => {
        console.error('Error submitting form:', error);
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerText = originalText;
        }
        // Fallback simulate submission if AJAX fails
        if (modalFormInner) modalFormInner.style.display = 'none';
        if (modalSuccess) modalSuccess.style.display = 'block';
      });
    });
  }
}

/* ==========================================================================
   9. Contact Form Simulation
   ========================================================================== */
function initContactForm() {
  const contactForm = document.getElementById('contact-us-form');
  if (!contactForm) return;

  const formInner = contactForm.querySelector('.contact-form-inner');
  const successScreen = contactForm.querySelector('.contact-form-success');

  contactForm.addEventListener('submit', (e) => {
    e.preventDefault();
    
    const formData = new FormData(contactForm);
    const submitBtn = contactForm.querySelector('button[type="submit"]');
    const originalText = submitBtn ? submitBtn.innerText : 'Transmit Message';
    
    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.innerText = 'Sending...';
    }

    fetch('https://formsubmit.co/ajax/nasrinjariwala176@gmail.com', {
      method: 'POST',
      body: formData
    })
    .then(response => response.json())
    .then(data => {
      if (submitBtn) {
        submitBtn.disabled = false;
        submitBtn.innerText = originalText;
      }
      if (formInner) formInner.style.display = 'none';
      if (successScreen) successScreen.style.display = 'block';
    })
    .catch(error => {
      console.error('Error submitting form:', error);
      if (submitBtn) {
        submitBtn.disabled = false;
        submitBtn.innerText = originalText;
      }
      // Fallback simulate submission if AJAX fails
      if (formInner) formInner.style.display = 'none';
      if (successScreen) successScreen.style.display = 'block';
    });
  });
}

/* ==========================================================================
   10. Newsletter Form Simulation
   ========================================================================== */
function initNewsletterForm() {
  const newsletterForms = document.querySelectorAll('.newsletter-form');
  
  newsletterForms.forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const input = form.querySelector('input');
      const originalHtml = form.innerHTML;
      
      if (input && input.value) {
        form.innerHTML = '<span style="color:#06B6D4; font-family:\'Outfit\', sans-serif; font-weight:600; font-size:0.95rem;">Subscribed! Check your inbox soon.</span>';
        
        setTimeout(() => {
          form.innerHTML = originalHtml;
          initNewsletterForm(); // Re-initialize events
        }, 5000);
      }
    });
  });
}
