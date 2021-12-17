function like(btn){
    data = btn.value.split(":")
    $.ajax({
        url: url_like,
        type: $(this).attr('post'),
        data: {"id":data[0],
            "typefors":data[1]},
        failure: function(data) { 
            alert('Error sory');
            console.log(data)
        }
    });
    btn.disabled=true
}