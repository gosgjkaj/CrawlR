$('#likes').click(function(){
    var routename;
    routename = $(this).attr("data-routename");
    $.get('/crawlr/like/', {route_slug: routename}, function(data){
        $('#like_count').html(data);
            $('#likes').hide();
            $('#button_used').show();
    });
});