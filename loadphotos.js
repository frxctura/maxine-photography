document.addEventListener('DOMContentLoaded', function() {
  const gallery = document.getElementById('photoGallery');
  const lightbox = document.getElementById('lightbox');
  const lightboxImage = document.getElementById('lightboxImage');
  const closeBtn = document.querySelector('.close');
  const prevBtn = document.querySelector('.prev');
  const nextBtn = document.querySelector('.next');

  let currentImageIndex = 0;
  const images = [];

  fetch('images.json')
    .then(response => response.json())
    .then(data => {
      data.images.forEach((imageData, index) => {
        const thumbnail = document.createElement('img');
        thumbnail.src = imageData.thumbnail;
        thumbnail.alt = `Thumbnail ${index + 1}`;
        thumbnail.addEventListener('click', function() {
          currentImageIndex = index;
          lightbox.style.display = 'flex';
          updateLightboxImage(imageData.fullSize);
        });
        gallery.appendChild(thumbnail);
        images.push(imageData.fullSize);
      });
    })
    .catch(error => console.error('Error fetching image data:', error));

  closeBtn.addEventListener('click', function() {
    lightbox.style.display = 'none';
    clearLightboxImage();
  });

  prevBtn.addEventListener('click', function() {
    showPreviousImage();
  });

  nextBtn.addEventListener('click', function() {
    showNextImage();
  });

  lightbox.addEventListener('click', function(event) {
    if (event.target === lightbox) {
      lightbox.style.display = 'none';
      clearLightboxImage();
    }
  });

  document.addEventListener('keydown', function(event) {
    if (lightbox.style.display === 'flex') {
      if (event.key === 'ArrowLeft') {
        showPreviousImage();
      } else if (event.key === 'ArrowRight') {
        showNextImage();
      } else if (event.key === 'Escape') {
        lightbox.style.display = 'none';
        clearLightboxImage();
      }
    }
  });

  function updateLightboxImage(src) {
    lightboxImage.src = ''; 
    setTimeout(() => {
      lightboxImage.src = src;  
    }, 50); 
  }

  function clearLightboxImage() {
    lightboxImage.src = '';
  }

  function showPreviousImage() {
    currentImageIndex = (currentImageIndex - 1 + images.length) % images.length;
    updateLightboxImage(images[currentImageIndex]);
  }

  function showNextImage() {
    currentImageIndex = (currentImageIndex + 1) % images.length;
    updateLightboxImage(images[currentImageIndex]);
  }
});
