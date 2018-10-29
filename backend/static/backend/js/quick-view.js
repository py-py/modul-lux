/*jQuery*/

(function ($) {
    // USE STRICT
    "use strict";
    var getProductInfo = function (idProduct, urlProduct) {
        $.get({
            url: urlProduct,
            data: {
                'id_product': idProduct
            },
            success: function (data) {
                console.log(data);
            }

        })
    };

    $('.btn-quickview').click(function () {
        var data = $(this).data();
        getProductInfo(data.id, data.url);
    });
})
(jQuery);

