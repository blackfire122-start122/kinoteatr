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