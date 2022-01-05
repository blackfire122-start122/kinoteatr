let users_div = document.querySelector(".user_all")

function btn_friend(id_btn){
	id_btn.disabled=true;
	$.ajax({
		type: $(this).attr('post'),
		url: url_ajax,
		data: {'id':id_btn.value},
		success: function (response) {
            id_btn.innerHTML=response.data_text;
        }
	})
}

function more_users(btn){
    btn.disabled=true
    $.ajax({
    	type: $(this).attr('post'),
        url: url_more_users,
        data: { "user_count":user_count+20,
                "user_count_end": user_count},
        failure: function(data) { 
            alert('Error sory')
        },
        success: function(data){
            users_div.insertAdjacentHTML('beforeend',data)
            btn.disabled=false
        }
    })
    user_count += 20
}