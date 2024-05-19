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
        data.images.forEach((image, index) => {
          const img = document.createElement('img');
          img.src = image;
          img.alt = `Photo ${index + 1}`;
          img.addEventListener('click', function() {
            currentImageIndex = index;
            lightbox.style.display = 'flex';
            lightboxImage.src = this.src;
          });
          gallery.appendChild(img);
          images.push(image);
        });
      })
      .catch(error => console.error('Error fetching image filenames:', error));
  
    closeBtn.addEventListener('click', function() {
      lightbox.style.display = 'none';
    });
  
    prevBtn.addEventListener('click', function() {
      currentImageIndex = (currentImageIndex - 1 + images.length) % images.length;
      lightboxImage.src = images[currentImageIndex];
    });
  
    nextBtn.addEventListener('click', function() {
      currentImageIndex = (currentImageIndex + 1) % images.length;
      lightboxImage.src = images[currentImageIndex];
    });
  
    lightbox.addEventListener('click', function(event) {
      if (event.target === lightbox) {
        lightbox.style.display = 'none';
      }
    });
  });
  