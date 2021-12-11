let l_v = document.getElementsByClassName('link_tgy')

function btn_sorts(btn){
	if (l_v[btn.value].style.display == "block"){
		l_v[btn.value].style.display = "none"
	}else{
		l_v[btn.value].style.display = "block"
	}

}