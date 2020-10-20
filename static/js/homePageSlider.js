 $(document).ready(function() {
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