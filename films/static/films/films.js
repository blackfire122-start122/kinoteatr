if (!video_film){
	let video_film = document.querySelector('#video_film')
}
function show_serias(btn){
    sezon_ser = document.getElementById(btn.value)
    sez=document.getElementById("sezons")
    sez.style.display='none'
    sezon_ser.style.display="flex"
}
function video_seria(btn){
    console.log(btn.value)
    video_film.src = btn.value
}

function toggleFullscreen(btn) {
  let video_fs = document.querySelector('.for_fs')
  if (!document.fullscreenElement) {
    video_fs.requestFullscreen().catch(err => {
      alert(`Error attempting to enable full-screen mode: ${err.message} (${err.name})`);
    });
  } else {
    document.exitFullscreen();
  }
  btn.style.display = "none"
}
