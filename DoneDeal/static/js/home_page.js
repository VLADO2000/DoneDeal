// Add animation on scroll
window.addEventListener('scroll', function() {
    const blocks = document.querySelectorAll('.why-us-block, .client-block, .membership-block');
  
    blocks.forEach(block => {
      const blockPosition = block.getBoundingClientRect().top;
      const windowHeight = window.innerHeight;
  
      if (blockPosition < windowHeight * 0.8) {
        block.classList.add('animate');
      } else {
        block.classList.remove('animate');
      }
    });
  });