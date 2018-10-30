/*jQuery*/

(function ($) {
    // USE STRICT
    "use strict";

    var instRemodal = $('[data-remodal-id=modal]').remodal();

    var getProductInfo = function (urlProduct) {
        $.get({
            url: urlProduct,
            success: function (data) {
                console.log(data);
            }

        })
    };

    $('.btn-quickview').click(function () {
        var data = $(this).data();
        getProductInfo(data.url);
    });
})
(jQuery);

