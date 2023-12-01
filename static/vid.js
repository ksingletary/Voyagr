// So that background video can play

var interval = setInterval(function(){
    var countForVideo = document.getElementById('vid').readyState;
    if(countForVideo == 4){
      document.getElementById('vid').play();
      clearInterval(interval);
    }
  }, 0);

  // Helper function for scroll animations

const elementsToFadeInUpOnScroll = document.querySelectorAll(".fadeInUp");
if (elementsToFadeInUpOnScroll) {
  window.addEventListener("scroll", function(event) {
    elementsToFadeInUpOnScroll.forEach(function(element) {
      if (window.scrollY >= (element.offsetTop - window.innerHeight)) {
        element.classList.add("fadeInUp");
      } else {
        element.classList.remove("fadeInUp");
      }
    });
  });
}