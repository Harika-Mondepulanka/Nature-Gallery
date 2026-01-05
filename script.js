const images = [
  {
    src: 'images/photo1.jpg',
    alt: 'Mountain Sunrise',
    story: 'Captured at dawn after a 3-hour hike. The mist rising from the valley made the moment unforgettable.'
  },
  {
    src: 'images/photo2.jpg',
    alt: 'Forest Trail',
    story: 'This trail winds through an ancient forest in the Pacific Northwest. The silence was profound.'
  }
  // Add more image objects as needed
];

function openLightbox(index) {
  const lightbox = document.getElementById('lightbox');
  const img = document.getElementById('lightbox-img');
  const story = document.getElementById('lightbox-story');

  img.src = images[index].src;
  img.alt = images[index].alt;
  story.textContent = images[index].story;

  lightbox.style.display = 'flex';
}

function closeLightbox() {
  document.getElementById('lightbox').style.display = 'none';
}