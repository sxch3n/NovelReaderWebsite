
$(".btn-search").on("click", function() {
    $(".input-search").toggleClass("inclicked");
    $(".btn-search").toggleClass("close");
});

$(".book").on("click", function() {
    alert("hello book");
});
$(document).ready(function(){
    $(".owl-carousel").owlCarousel();
  });