let films_div = document.querySelector(".films")

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

function more_films(btn){
    btn.disabled=true
    $.ajax({
        url: url_more_films,
        type: $(this).attr('post'),
        data: { "str_url_type":str_url_type,
                "str_url_genre":str_url_genre,
                "str_year":str_year,
                "films_count":films_count+20,
                "films_count_end": films_count},
        failure: function(data) { 
            alert('Error sory')
        },
        success: function(data){
            films_div.insertAdjacentHTML('beforeend',data)
            btn.disabled=false
        }
    })
    films_count += 20
}