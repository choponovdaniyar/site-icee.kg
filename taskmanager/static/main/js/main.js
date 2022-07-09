$(".burger__icon").on("click", function(){
    $(".burger__line-1").toggleClass("burger__line-1_active");
    $(".burger__line-2").toggleClass("burger__line-2_active");
    $(".burger__line-3").toggleClass("burger__line-3_active");
    $(".burger__items").slideToggle(200);
})

$(".exit").on("click", function(){
    $('.spiker-modal').css({
        "display": "none"
    })
})

$(".spiker").on("click", function(){
    let modal = $(this).next();
    $(modal).css({
        "display": "flex"
    })
})

$(".spiker__img").height(
  $(".spiker__img").width() * (4/3)
);



setInterval(() => {
    let bodyH = $("body").height();
    let windowH = $(window).height();
    if( windowH > bodyH){
        let context = $("body").children()[1];
        let contextH = windowH - $("footer").height();
        $(context).height(contextH);
    }
}, 100)
