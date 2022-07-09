$(".accordion").on("click", function(){
    $(this).toggleClass("accordion-active");
    $(this).next().slideToggle(200);
})