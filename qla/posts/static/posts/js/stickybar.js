jQuery(document).ready(function() {
    
    var navOffSet = jQuery("nav").offset().top;
//    alert(navOffSet);
    
    jQuery("nav").wrap('<div class="nav-placeholder"></div>');
    jQuery(".nav-placeholder").height(jQuery("nav").outerHeight());
    jQuery("nav").wrapInner('<div class="nav-inner"></div>');
    
    jQuery(window).scroll(function(){
    
        var scrollPos = $(window).scrollTop();
        if (scrollPos >= navOffSet){
            jQuery("nav").addClass('fixedTop');
        }
        else{
            jQuery("nav").removeClass('fixedTop');
        }
    });

});