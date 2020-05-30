
$(".btn-search").on("click", function() {
    $(".input-search").toggleClass("inclicked");
    $(".btn-search").toggleClass("close");
});


$(document).ready(function(){
    $(".owl-carousel").owlCarousel({
        margin:10,
        responsive:{            
            0:{item:1,},
            600:{item:3}
        }
    });
  });