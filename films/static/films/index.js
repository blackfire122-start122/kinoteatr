let connectButton = document.querySelector('#connectButton')
let divMsg = document.querySelector('#div_message')
let btnCreateChat = document.querySelector('#btnCreateChat')
let chatLog = document.querySelector('#chat-log')
let acceptDiv = document.querySelector('#acceptDiv')
let msg_user = document.querySelector('#messageInput')
let send_mes_btn = document.querySelector('#sendmesbtn')
let video_film = document.querySelector('#video_film')
let img_camera = document.querySelector('#img_camera')
let raw = document.querySelector('#raw')
let friend = document.querySelector('#friends_block')
let com_user = document.querySelector('#comment_user')

let conn;
let pc;
let dataChannel;
let friend_name = My_name
let currentTime_film = false
let id_call

let localStream = new MediaStream()

let config = {
    iceServers: [
        {
            "urls": "stun:stun.l.google.com:19302",
        }
    ]
};

const constraints = {
    video: true,
    audio: false
};

function connect() {
    // conn = new WebSocket('wss://'+location.hostname +'/'+ friend_name+film_id)
    conn = new WebSocket('ws://127.0.0.1:8000/' + friend_name+film_id)
    conn.addEventListener('open', (e) => {
        console.log("Connected to the signaling server "+friend_name);
        initialize(My_name);
    })
    conn.addEventListener('message', onmessage)
    connectButton.style.display = 'none'
    send_mes_btn.style.display = 'inline-block'
    friend.style.display = 'none'

}

function onmessage(msg) {
    let content = JSON.parse(msg.data)
    let data = content.data
    if (content.peer === My_name) {
        return;
    }
    switch (content.event) {
        case "offer":
            handleOffer(data)
            break;
        case "answer":
            handleAnswer(data)
            break;
        case "candidate":
            handleCandidate(data)
            break;
        default:
            break;
    }
}

function send(message) {
    conn.send(JSON.stringify(message))
}
function send_on_dc(message) {
    dataChannel.send(JSON.stringify(message))
}
function initialize(username) {
    pc = new RTCPeerConnection(config)
    pc.onicecandidate = function (event) {
        if (event.candidate) {
            send({
                peer: username,
                event: "candidate",
                data: event.candidate
            });
        }
    };

    dataChannel = pc.createDataChannel("dataChannel")

    dataChannel.onerror = function (error) {
        console.log("Error occured on datachannel:", error)
    }

    dataChannel.onmessage = function (event) {
        data = JSON.parse(event.data)
        keys = Object.keys(data)

        if (data[keys[0]]=='pause'){
            video_film.pause()
            return
        }else if (data[keys[0]]=='play'){
            video_film.play()
            return
        }
        else if (data[keys[0]]=='seeked') {
            currentTime_film = true
            video_film.currentTime = data[keys[1]]
            setTimeout(function (){
                currentTime_film = false
            },100)
            return
        }else if (keys[0]=='connect_on_id'){
            id_call = data[keys[0]]
            return
        }else if(keys[0]=='no_video'){
            let video_call_stream = document.getElementById(data[keys[0]])
            raw.removeChild(video_call_stream)
            return
        }
        chatLog.value += (event.data + '\n')
    }

    dataChannel.onclose = function () {
        console.log("disconnected")
    }

    pc.ondatachannel = function (event) {
        dataChannel = event.channel
        send_on_dc({"connect_on_id": My_id})
    }
    CreateOffer()
}

function CreateOffer(){
    if (localStream) {
        localStream.getTracks().forEach(track => {
            pc.addTrack(track, localStream)
        })
    }
    pc.createOffer(function (offer) {
        send({
            peer: My_name,
            event: "offer",
            data: offer
        });
        pc.setLocalDescription(offer);
    }, function (error) {
        alert("Error creating an offer");
    })
}

function handleOffer(offer) {
    let remoteStream = new MediaStream();

    pc.addEventListener('track', async (event) => {
        remoteStream.addTrack(event.track)
    })

    pc.setRemoteDescription(offer)
        .then(() => {
            console.log('Set Remote Description for offer');
            return pc.createAnswer()
        })
        .then(answer => {
            console.log('Answer create from offer');
            pc.setLocalDescription(answer)

            send({
                peer: friend_name,
                event: "answer",
                data: answer
            })
        })
    if_id = setInterval(function (){
        if (id_call && dataChannel.readyState == 'open'){
            add_videoelement(remoteStream,id_call)
            id_call = null
            clearInterval(if_id);
        }
    },10)
}

function handleCandidate(candidate) {
    pc.addIceCandidate(new RTCIceCandidate(candidate));
}

function handleAnswer(answer) {
    remoteStream = new MediaStream()
    pc.addEventListener('track', async (event) => {
        remoteStream.addTrack(event.track)
    })
    pc.setRemoteDescription(new RTCSessionDescription(answer))
        .then(() => {
            console.log('Set Remote Description for', friend_name)
            return pc.createAnswer()
        })
        .then(answer => {
            console.log('Answer create from '+friend_name)
            pc.setLocalDescription(answer)
        })
    if_id = setInterval(function (){
        if (id_call && dataChannel.readyState == 'open'){
            add_videoelement(remoteStream,id_call)
            id_call = null
            clearInterval(if_id);
        }
    },10)
}

function sendMessage() {
    send_on_dc({"My_name":msg_user.value})
    chatLog.value += (My_name+': '+msg_user.value + '\n')
    msg_user.value = ''
}

function my_stream() {
    navigator.mediaDevices.getUserMedia(constraints)
        .then(stream => {
            localStream = stream
            add_videoelement(localStream,0)
            let audioTrack = stream.getAudioTracks()
            let videoTrack = stream.getVideoTracks()
            // audioTrack[0].enabled = true
            videoTrack[0].enabled = true
        }).catch(error => {
        console.log('Error media', error)
    })
}

function conn_user(btn){
    friend_name = btn.value
    connect()
}

function turn_camera(btn){
    if (btn.value == 'off'){
        let video_my_stream = document.querySelector('#my_stream_div')

        btn.value = 'on'
        btn.style.background = '#8EABEC'
        img_camera.src = camera_none_img

        localStream.getTracks().forEach(function(track) {
          track.stop()
        })
        raw.removeChild(video_my_stream)
        const senders = pc.getSenders()
        senders.forEach((sender) => pc.removeTrack(sender))
        if (dataChannel){
            send_on_dc({'no_video':My_id})
        }
        return
    }

    btn.value = 'off'
    btn.style.background = 'red'
    img_camera.src = camera_img
    my_stream()
    if (dataChannel){
        CreateOffer()
        send_on_dc({"connect_on_id": My_id})
    }
}

function add_videoelement(srcObject_video,id=1) {
    let video_element = document.createElement('video');
    video_element.className = "video_people"
    video_element.autoplay = true
    video_element.width = 200
    video_element.id = id
    video_element.srcObject = srcObject_video
    video_element.muted = true

    if (video_element.id==0){
        let div = document.createElement('div');
        let h2 = document.createElement('h2');
        h2.textContent = "You"
        h2.style.position = 'absolute'
        h2.style.color = "white"
        div.id = 'my_stream_div'
        div.append(h2)
        div.append(video_element)
        raw.append(div)
        return
    }

    raw.append(video_element)
}

video_film.addEventListener('pause',function(){
    send_on_dc({'video':'pause'})
})
video_film.addEventListener('play',function(){
    send_on_dc({'video':'play'})
})
video_film.addEventListener('seeked',function(){
    if (!currentTime_film) {
        send_on_dc({'video':'seeked','time':video_film.currentTime})
    }
})

video_film.addEventListener('webkitfullscreenchange', function(){
    console.log(video_film.style)
})

let id_com
let style_div
function btn_reply_ajax(btn){
    btn.parentNode.parentNode.parentNode.style.background = 'rgba(0, 0, 0, 0.5)'
    style_div = btn.parentNode.parentNode.parentNode
    id_com = btn.value
}

function comment(){
    if (!com_user.value){
        return
    }
    $.ajax({
        url: comment_ajax,
        type: $(this).attr('post'),
        data: {"typefors":type_fs,
            "comment":com_user.value,
                "id":film_id,
                "id_com":id_com},
        failure: function(data) { 
            alert(data)
        }
    })
    id_com = null
    if (style_div){
        style_div.style.background = 'rgba(0, 0, 0, 0.0)'
        style_div = null
    }
    com_user.value = ""
}

function comment_delete(btn){
    $.ajax({
        url: comment_delete_ajax,
        type: $(this).attr('post'),
        data: {"id":btn.value},
        failure: function(data) { 
            alert(data)
        }
    })
}