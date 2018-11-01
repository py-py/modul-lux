(function ($) {
    // USE STRICT
    "use strict";

    let fillModalWindow = function (data) {
         $('#idProductName').text(data.name);
         $('#idProductName').attr('href', data.url_product_detail);
         $('#idProductDescription').text(data.description);
         $('#idProductViewFullDetails').attr('href', data.url_product_detail);

         $('#idProductImages').find('.image-box').remove();
         for (let image of data.images) {
             $('<div class="image-box"><img src="' + image.url + '"></div>').prependTo($('#idProductImages'));
         }
         $('.owl-carousel').owlCarousel();
    };


    let instRemodal = $('[data-remodal-id="quickview"]').remodal();

    let getProductInfo = function (urlProduct) {
        $.get({
            url: urlProduct,
            success: function (data) {
                fillModalWindow(data);
                instRemodal.open();
            }
        })
    };

    $('.btn-quickview').click(function () {
        let data = $(this).data();
        getProductInfo(data.url);
    });

})
(jQuery);


