function like(btn){
    $.ajax({
        url: url_like,
        type: $(this).attr('post'),
        data: {"id":btn.value},
        failure: function(data) { 
            alert('Error sory');
            console.log(data)
        }
    });
    btn.disabled=true
}