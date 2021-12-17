username_form = document.getElementById('username')
first_name_form = document.getElementById('first_name')
last_name_form = document.getElementById('last_name')
email_form = document.getElementById('email')
age_form = document.getElementById('age')
country_form = document.querySelector('#id_country > option:nth-child(1)')

username_form.value=user_username
first_name_form.value=user_first_name
last_name_form.value=user_last_name
email_form.value=user_email
age_form.value=user_age

function btn_friend_add(btn){
	$.ajax({
		type: $(this).attr('post'),
		url: url_ajax_add,
		data: {'id':btn.value},
		success: function (response) {
            console.log(response.data_text)
        }
	})
	btn.disabled=true;
	btn.display='none';
}
function btn_friend_no_add(btn){
	$.ajax({
		type: $(this).attr('post'),
		url: url_ajax_no_add,
		data: {'id':btn.value},
	})
	btn.disabled=true;
	btn.display='none';
}
function dont_like(btn){
	data = btn.value.split(":")
	$.ajax({
		type: $(this).attr('post'),
		url: dont_like_url,
		data: {'id':data[0],"typefors":data[1]},
	})
}
function exit(btn){
	$.ajax({
		type: $(this).attr('post'),
		url: ajax_exit,
		success: function (data){
			if(data.status == 200)
				window.location.href = data.url
		}
	})
}

function btn_no_friend(btn){
	$.ajax({
		type: $(this).attr('post'),
		url: no_friend_ajax,
		data: {'id':btn.value},
		success: function (data){
			console.log(data)
		}
	})
}

country_form.text=user_country