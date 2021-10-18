// Run when an article is clicked
document.addEventListener('DOMContentLoaded', function(){
    document.querySelectorAll('#article').forEach(button =>{
        button.onclick = function() {
            openArticle(this.dataset.id)
        }
    })
    // console.log($('.owl-carousel'))
    var owl = $('.owl-one');
    owl.owlCarousel({
        items:1,
        loop:true,
        margin:10,
        autoplay:true,
        autoplayTimeout:4000,
        autoplayHoverPause:true,
        dots: false,
    });
    $('.play').on('click',function(){
        owl.trigger('play.owl.autoplay',[4000])
    })
    $('.stop').on('click',function(){
        owl.trigger('stop.owl.autoplay')
    })
    $('.owl-two').owlCarousel({
        loop:true,
        margin:10,
        responsiveClass:true,
        responsive:{
            0:{
                items:1,
            },
            600:{
                items:2,
            },
            1000:{
                items:3,
            }
        }
    })
    
    $(document).ready(function(){
        var submitIcon = $('.searchbar-icon');
        var inputBox = $('.searchbar-input');
        var searchbar = $('.searchbar');
        var isOpen = false;
        submitIcon.click(function(){
        if(isOpen == false){
            searchbar.addClass('searchbar-open');
            inputBox.focus();
            isOpen = true;
        } else {
            searchbar.removeClass('searchbar-open');
            inputBox.focusout();
            isOpen = false;
        }
        });
            submitIcon.mouseup(function(){
            return false;
        });
            searchbar.mouseup(function(){
            return false;
        });
        $(document).mouseup(function(){
        if(isOpen == true){
            $('.searchbar-icon').css('display','block');
            submitIcon.click();
        }
        });
        });
        function buttonUp(){
        var inputVal = $('.searchbar-input').val();
        inputVal = $.trim(inputVal).length;
        if( inputVal !== 0){
            $('.searchbar-icon').css('display','none');
        } else {
            $('.searchbar-input').val('');
            $('.searchbar-icon').css('display','block');
        }
    }
    
})


function openArticle(id){
    console.log("click")
    document.location.href = "/article/" + id;
}