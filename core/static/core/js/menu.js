
let btnMenu=document.getElementById('btnmenu');
let menu=document.getElementById('menu');
btnMenu.addEventListener('click',function(){
    'user strict';
    menu.classList.toggle('mostrar');
 
});

const carousel = document.querySelector('.carousel');
const slides = carousel.querySelectorAll('.slide');
const prevButton = carousel.querySelector('.prev');
const nextButton = carousel.querySelector('.next');
let currentSlide = 0;

prevButton.addEventListener('click', () => {
  slides[currentSlide].classList.remove('active');
  currentSlide = (currentSlide - 1 + slides.length) % slides.length;
  slides[currentSlide].classList.add('active');
});

nextButton.addEventListener('click', () => {
  slides[currentSlide].classList.remove('active');
  currentSlide = (currentSlide + 1) % slides.length;
  slides[currentSlide].classList.add('active');
});




