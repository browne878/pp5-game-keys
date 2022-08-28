// Change highlighted category in the in the top menu
$('#catagories-container').children('ul').children('li').on('click', function () {
    $('#catagories-container').children('ul').children('li').children('a').removeClass('active');
    const cat = $(this).children()[0];
    $(cat).addClass('active');
});