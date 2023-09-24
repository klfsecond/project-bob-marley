(function ($) {
    "use strict";

    //Preloader
    $(window).on('load', function (event) {
        $('.js-preloader').delay(500).fadeOut(500);
    });
    
    //Counter
    $(".odometer").appear(function (e) {
        var odo = $(".odometer");
        odo.each(function () {
            var countNumber = $(this).attr("data-count");
            $(this).html(countNumber);
        });
    });

    // Language Dropdown
    $(".language-option").each(function () {
        var each = $(this)
        each.find(".lang-name").html(each.find(".language-dropdown-menu a:nth-child(1)").text());
        var allOptions = $(".language-dropdown-menu").children('a');
        each.find(".language-dropdown-menu").on("click", "a", function () {
            allOptions.removeClass('selected');
            $(this).addClass('selected');
            $(this).closest(".language-option").find(".lang-name").html($(this).text());
        });
    })

    // //Tweenmax js
    $('.hero-wrap.style1').mousemove(function (e) {
        var wx = $(window).width();
        var wy = $(window).height();
        var x = e.pageX - this.offsetLeft;
        var y = e.pageY - this.offsetTop;
        var newx = x - wx / 2;
        var newy = y - wy / 2;
        $('.hero-content').each(function () {
            var speed = $(this).attr('data-speed');
            if ($(this).attr('data-revert')) speed *= -.4;
            TweenMax.to($(this), 1, { x: (1 - newx * speed), y: (1 - newy * speed) });
        });
    });
    
    //Counter
    $(".odometer").appear(function (e) {
        var odo = $(".odometer");
        odo.each(function () {
            var countNumber = $(this).attr("data-count");
            $(this).html(countNumber);
        });
    });

    //Hero  Slider 
    $(".hero-property-slider").owlCarousel({
        nav: true,
        dots: false,
        loop: true,
        margin: 10,
        items: 1,
        navText: ['<i class="flaticon-arrow-left"></i>', '<i class="flaticon-right-arrow-3"></i>'],
        thumbs: false,
        smartSpeed: 1300,
        autoplay: false,
        autoplayTimeout: 4000,
        autoplayHoverPause: false,
        responsiveClass: true,
        autoHeight: true,
        responsive: {
            0: {
                items: 1,
                margin:5,
            },
            768: {
                items: 2,

            },
            992: {
                items: 1,

            },
            1200: {
                items: 2,
                margin:5,
            },
            1400: {
                items: 2,
                margin:10,
            }
        }
    });
    $(".hero-slider-one").owlCarousel({
        nav: true,
        dots: false,
        loop: true,
        margin: 20,
        items: 1,
        navText: ['<i class="flaticon-back"></i>', '<i class="flaticon-next-1"></i>'],
        thumbs: false,
        smartSpeed: 1300,
        autoplay: false,
        autoplayTimeout: 4000,
        autoplayHoverPause: false,
        responsiveClass: true,
        autoHeight: true,
    });
    $(".hero-slider-two").owlCarousel({
        nav: true,
        dots: false,
        loop: true,
        margin: 0,
        items: 1,
        navText: ['<i class="flaticon-back"></i>', '<i class="flaticon-next-1"></i>'],
        thumbs: false,
        smartSpeed: 1300,
        autoplay: false,
        autoplayTimeout: 4000,
        autoplayHoverPause: false,
        responsiveClass: true,
        autoHeight: true,
    });

    //Property Image Slider
    $(".property-img-slider").owlCarousel({
        nav: true,
        dots: false,
        loop: true,
        margin: 20,
        items: 1,
        navText: ['<i class="ri-arrow-left-s-line"></i>', '<i class="ri-arrow-right-s-line"></i>'],
        thumbs: false,
        smartSpeed: 1300,
        autoplay: false,
        autoplayTimeout: 4000,
        autoplayHoverPause: false,
        responsiveClass: true,
        autoHeight: true,
    });
    $(".property-slider-one").owlCarousel({
        nav: false,
        dots: true,
        loop: true,
        margin: 20,
        items: 1,
        smartSpeed: 1300,
        autoplay: false,
        autoplayTimeout: 4000,
        autoplayHoverPause: false,
        responsiveClass: true,
        autoHeight: true,
        responsive: {
            0: {
                items: 1,
                margin:5,

            },
            768: {
                items: 2,

            },
            992: {
                items: 2,

            },
            1200: {
                items: 3,

            }
        }
    });
    $(".property-slider-two").owlCarousel({
        nav: false,
        dots: true,
        loop: true,
        margin: 20,
        items: 1,
        smartSpeed: 1300,
        autoplay: false,
        autoplayTimeout: 4000,
        autoplayHoverPause: false,
        responsiveClass: true,
        autoHeight: true,
        responsive: {
            0: {
                items: 1,
                margin:5,

            },
            768: {
                items: 2,

            },
            992: {
                items: 2,

            },
            1200: {
                items: 3,

            }
        }
    });
    $(".property-slider-three").owlCarousel({
        nav: false,
        dots: true,
        loop: true,
        margin: 25,
        items: 1,
        center:true,
        smartSpeed: 1300,
        autoplay: false,
        autoplayTimeout: 4000,
        autoplayHoverPause: false,
        responsiveClass: true,
        autoHeight: true,
        responsive: {
            0: {
                items: 1,

            },
            768: {
                items: 1.8,

            },
            992: {
                items: 2.2,

            },
            1200: {
                items: 2.6,
            },
            1400: {
                items: 3.5,
            },
            1600: {
                items: 4.1,
            }
        }
    });

    //City Slider
    $(".city-slider-one").owlCarousel({
        nav: false,
        dots: true,
        loop: true,
        margin: 20,
        items: 1,
        smartSpeed: 1300,
        autoplay: false,
        autoplayTimeout: 4000,
        autoplayHoverPause: false,
        responsiveClass: true,
        autoHeight: true,
        responsive: {
            0: {
                items: 1,
                margin:5,

            },
            768: {
                items: 2,

            },
            992: {
                items: 2,

            },
            1200: {
                items: 3,
            }
        }
    });
    $(".city-slider-two").owlCarousel({
        nav: false,
        dots: true,
        loop: true,
        margin: 20,
        center:true,
        smartSpeed: 1300,
        autoplay: false,
        autoplayTimeout: 4000,
        autoplayHoverPause: false,
        responsiveClass: true,
        autoHeight: true,
        responsive: {
            0: {
                items: 1,
            },
            768: {
                items: 2,
            },
            992: {
                items: 2.6,

            },
            1200: {
                items:3.5,
            },
            1400: {
                items:3.6,
            }
        }
    });

    //Testimonial Slider 
    $(".testimonial-slider-one").owlCarousel({
        nav: false,
        dots: true,
        loop: true,
        margin: 10,
        items: 1,
        thumbs: false,
        smartSpeed: 1300,
        autoplay: false,
        autoplayTimeout: 4000,
        autoplayHoverPause: false,
        responsiveClass: true,
        autoHeight: true,
        responsive: {
            0: {
                items: 1,
                margin:5,

            },
            768: {
                items: 2,

            },
            992: {
                items: 2,

            },
            1200: {
                items: 3,

            }
        }
    });
    $(".testimonial-slider-two").owlCarousel({
        nav: true,
        dots: false,
        loop: true,
        margin: 10,
        items: 1,
        navText: ['<i class="flaticon-back"></i>', '<i class="flaticon-next-1"></i>'],
        thumbs: false,
        smartSpeed: 1300,
        autoplay: false,
        autoplayTimeout: 4000,
        autoplayHoverPause: false,
        responsiveClass: true,
        autoHeight: true,
        responsive: {
            0: {
                items: 1,
                margin:5,

            },
            768: {
                items: 2,

            },
            992: {
                items: 2,

            },
            1200: {
                items: 2.8,

            }
        }
    });
    $(".testimonial-slider-three").owlCarousel({
        nav: false,
        dots: true,
        loop: true,
        margin: 15,
        items: 1,
        center:true,
        thumbs: false,
        smartSpeed: 1300,
        autoplay: false,
        autoplayTimeout: 4000,
        autoplayHoverPause: false,
        responsiveClass: true,
        autoHeight: true,
        responsive: {
            0: {
                items: 1,

            },
            768: {
                items: 1.8,

            },
            992: {
                items: 2.4,

            },
            1200: {
                items: 2.8,
            },
            1400: {
                items: 4.1,

            }
        }
    });

    //Partner Slider
    $(".partner-slider").owlCarousel({
        nav: false,
        dots: false,
        loop: true,
        margin: 15,
        items: 1,
        thumbs: false,
        smartSpeed: 1300,
        autoplay: true,
        autoplayTimeout: 4000,
        autoplayHoverPause: false,
        responsiveClass: true,
        autoHeight: true,
        responsive: {
            0: {
                items: 2,
            },
            768: {
                items: 3,
            },
            992: {
                items: 4,
            },
            1200: {
                items: 5,
            }
        }
    });

    //Video Slider
    var bigimage = $("#big");
    var thumbs = $("#thumbs");
    var syncedSecondary = true;
      
    bigimage
        .owlCarousel({
        items: 1,
        nav: false,
        smartSpeed: 1300,
        autoplay: true,
        dots: false,
        loop: true,
        autoplay: true,
        autoplayTimeout: 4000,
        autoplayHoverPause: false,
        responsiveClass: true,
        autoHeight: true,
        responsiveRefreshRate: 200
    })
        .on("changed.owl.carousel", syncPosition);
    
    thumbs
        .on("initialized.owl.carousel", function() {
        thumbs
        .find(".owl-item")
        .eq(0)
        .addClass("current");
    })

    .owlCarousel({
        items: 3,
        dots: false,
        nav: true,
        navText:  ['<i class="ri-arrow-left-s-line"></i>', '<i class="ri-arrow-right-s-line"></i>'],
        smartSpeed: 200,
        slideSpeed: 500,
        slideBy: 4,
        margin: 25,
        thumbs: false,
        smartSpeed: 1300,
        autoplay: true,
        autoplayTimeout: 4000,
        autoplayHoverPause: false,
        responsiveClass: true,
        autoHeight: true,
        responsiveRefreshRate: 100,
        responsive: {
            0: {
                items: 2,
                margin:15,
            },
            768: {
                items: 3,
            },
        }
    })
        .on("changed.owl.carousel", syncPosition2);
      
    function syncPosition(el) {
        var count = el.item.count - 1;
        var current = Math.round(el.item.index - el.item.count / 2 - 0.5);
    
        if (current < 0) {
        current = count;
        }
        if (current > count) {
        current = 0;
        }
        //to this
        thumbs
        .find(".owl-item")
        .removeClass("current")
        .eq(current)
        .addClass("current");
        var onscreen = thumbs.find(".owl-item.active").length - 1;
        var start = thumbs
        .find(".owl-item.active")
        .first()
        .index();
        var end = thumbs
        .find(".owl-item.active")
        .last()
        .index();
    
        if (current > end) {
        thumbs.data("owl.carousel").to(current, 100, true);
        }
        if (current < start) {
        thumbs.data("owl.carousel").to(current - onscreen, 100, true);
        }
    }
    
    function syncPosition2(el) {
        if (syncedSecondary) {
        var number = el.item.index;
        bigimage.data("owl.carousel").to(number, 100, true);
        }
    }
    
    thumbs.on("click", ".owl-item", function(e) {
        e.preventDefault();
        var number = $(this).index();
        bigimage.data("owl.carousel").to(number, 300, true);
    });
    
    // Price Range Slider
    $("#slider-range").slider({
        range: true,
        min: 0,
        max: 8000,
        values: [1200, 3000],
        slide: function (event, ui) {
           $("#amount_one").val(ui.values[0] + " - " + " KM" + ui.values[1] );
        }
    });
    $("#amount_one").val("KM " + $("#slider-range").slider("values", 0) +
        " - " + "KM " +  $("#slider-range").slider("values", 1));

    //sticky Header
    var wind = $(window);
    var sticky = $('.header-wrap');
    wind.on('scroll', function () {
        var scroll = wind.scrollTop();
        if (scroll < 100) {
            sticky.removeClass('sticky');
        } else {
            sticky.addClass('sticky');
        }
    });

    // Responsive mmenu
    $(window).on('resize', function() {
        if($(window).width() <= 1199) {
            $('.collapse.navbar-collapse').removeClass('collapse');
        }else{
            $('.navbar-collapse').addClass('collapse');
        }
    });
    $('.mobile-menu a').on('click', function() {
        $('.main-menu-wrap').addClass('open');
        $('.collapse.navbar-collapse').removeClass('collapse');
    });

    $('.mobile_menu a').on('click', function () {
        $(this).parent().toggleClass('open');
        $('.main-menu-wrap').toggleClass('open');
    });

    $('.menu-close').on('click', function () {
        $('.main-menu-wrap').removeClass('open')
    });
    $('.mobile-top-bar').on('click', function () {
        $('.header-top').addClass('open')
    });
    $('.close-header-top button').on('click', function () {
        $('.header-top').removeClass('open')
    });
    var $offcanvasNav = $('.navbar-nav'),
    $offcanvasNavSubMenu = $offcanvasNav.find('.dropdown-menu');
    $offcanvasNavSubMenu.parent().prepend('<span class="menu-expand"><i class="ri-arrow-down-s-line"></i></span>');
    $offcanvasNavSubMenu.slideUp();
    $offcanvasNav.on('click', 'li a, li .menu-expand', function (e) {
        var $this = $(this);
        if (($this.attr('href') === '#' || $this.hasClass('menu-expand'))) {
            e.preventDefault();
            if ($this.siblings('ul:visible').length) {
                $this.siblings('ul').slideUp('slow');
            } else {
                $this.closest('li').siblings('li').find('ul:visible').slideUp('slow');
                $this.siblings('ul').slideDown('slow');
            }
        }
        if ($this.is('a') || $this.is('span') || $this.attr('class').match(/\b(menu-expand)\b/)) {
            $this.parent().toggleClass('menu-open');
        } else if ($this.is('li') && $this.attr('class').match(/\b('dropdown-menu')\b/)) {
            $this.toggleClass('menu-open');
        }
    });

    // Scroll animation
    AOS.init();

    //Back To top
    function BackToTop() {
        $('.back-to-top').on('click', function () {
            $('html, body').animate({
                scrollTop: 0
            }, 100);
            return false;
        });

        $(document).scroll(function () {
            var y = $(this).scrollTop();
            if (y > 600) {
                $('.back-to-top').fadeIn();
                $('.back-to-top').addClass('open');
            } else {
                $('.back-to-top').fadeOut();
                $('.back-to-top').removeClass('open');
            }
        });
    }
    BackToTop();

})(jQuery);


// function to set a given theme/color-scheme
function setTheme(themeName) {
    localStorage.setItem('fela_theme', themeName);
    document.documentElement.className = themeName;
}

// function to toggle between light and dark theme
function toggleTheme() {
    if (localStorage.getItem('fela_theme') === 'theme-dark') {
        setTheme('theme-light');
    } else {
        setTheme('theme-dark');
    }
}

// Immediately invoked function to set the theme on initial load
(function () {
    if (localStorage.getItem('fela_theme') === 'theme-dark') {
        setTheme('theme-dark');
        document.getElementById('slider').checked = false;
    } else {
        setTheme('theme-light');
        document.getElementById('slider').checked = true;
    }
})();