$(document).ready(function () {
    $('#imageGallery').lightSlider({
        gallery: false,
        mode: 'fade',
        item: 1,
        auto: true,
        loop: true,
        slideMargin: 0,
        enableDrag: true,
        speed: 500,
        controls: false,
        pager: false,
        keyPress: true,
        adaptiveHeight: true,

    });
});

$(document).ready(function () {
    gridGallery({
        selector: "#horizontal-dark",
        darkMode: true,
        layout: "horizontal",
        gapLength: 4,
        rowHeight: 350,
        columnWidth: 400
    });

});

$(".gallery-image").bind("click", function () {
    let src = $(this).attr("src");
    src = src.replace('thumb', 'large')
    $(this).attr("src", src);

});
