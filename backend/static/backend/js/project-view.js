(function ($) {
    // USE STRICT
    "use strict";
    let destroyCarousel = function () {
        $('.owl-carousel').empty();
        $('.owl-carousel').owlCarousel('destroy');
    };

    let initCarousel = function () {
        var owlSelector = $('.owl-carousel');
        owlSelector.each(function () {
            var option = {
                items: 3,
                margin: 0,
                loop: false,
                center: false,
                mousedrag: true,
                touchdrag: true,
                pulldrag: true,
                autowidth: false,
                nav: false,
                navtext: ["<i data-toggle='tooltip' title='Previous' class='fa fa-angle-left'></i>", "<i data-toggle='tooltip' title='Next' class='fa" +
                " fa-angle-right'></i>"],
                dots: false,
                dotsdata: false,
                autoplay: false,
                smartspeed: 650,
                animateout: null,
                animatein: null,
                xs: 1,
                sm: 2,
                md: 2,
                lg: 3
            };

            for (var k in option) {
                if (option.hasOwnProperty(k)) {
                    if ($(this).attr('data-carousel-' + k) != null) {
                        option[k] = $(this).data('carousel-' + k);
                    }
                }
            }


            $(this).owlCarousel({
                margin: option.margin,
                loop: option.loop,
                center: option.center,
                mouseDrag: option.mousedrag,
                touchDrag: option.touchdrag,
                pullDrag: option.pulldrag,
                nav: option.nav,
                navText: option.navtext,
                dots: option.dots,
                dotsData: option.dotsdata,
                autoplay: option.autoplay,
                smartSpeed: option.smartspeed,
                animateIn: option.animatein,
                animateOut: option.animateout,
                autoWidth: option.autowidth,
                responsive: {
                    // breakpoint from 0 up
                    0: {
                        items: option.xs
                    },
                    // breakpoint from 768 up
                    480: {
                        items: option.sm,
                        autoplay: false,
                        touchDrag: false,
                        pullDrag: false
                    },
                    // breakpoint from 768 up
                    768: {
                        items: option.md
                    },
                    992: {
                        items: option.lg
                    },
                    1200: {
                        items: option.items
                    }
                }
            });

        });
        owlSelector.on('refreshed.owl.carousel', function () {
            $.fn.matchHeight._update();
        });
    };

    let openModalWindow = function () {
        $('[data-remodal-id="modalWindow"]').remodal().open();
    };

    let fillModalWindow = function (data) {
        $('#idProductName').text(data.name);
        $('#idProductName').attr('href', data.url_product_detail);

        $('#idProductDescription').text(data.description);
        $('#idProductViewFullDetails').attr('href', data.url_product_detail);

        $('#idProductImages').empty();
        $('#idProductImages').find('.image-box').remove();
        for (let image of data.images) {
            $('<img src="' + image.url + '">').prependTo($('#idProductImages'));
        }
    };

    let getProductData = function (urlProduct) {
        return $.get({
            url: urlProduct,
            success: function (productData) {
                fillModalWindow(productData);
                initCarousel();
                openModalWindow();
            }
        });
    };

    $('.btn-quickview').click(function (event) {
        event.preventDefault();
        let tagData = $(this).data();

        destroyCarousel();
        getProductData(tagData.url);
    });

})
(jQuery);


