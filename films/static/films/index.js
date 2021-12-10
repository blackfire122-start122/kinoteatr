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

let conn;
let peerConnection;
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
    conn = new WebSocket('ws://127.0.0.1:8000/chat/' + friend_name)
    conn.addEventListener('open', (e) => {
        console.log("Connected to the signaling server "+friend_name);
        initialize(My_name);
    })
    conn.addEventListener('message', onmessage)
    // send({
    //     peer: username,
    //     message: "My id",
    // });
    connectButton.style.display = 'none'
    send_mes_btn.style.display = 'inline-block'
}

function onmessage(msg) {
    let content = JSON.parse(msg.data);
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

function initialize(username) {
    peerConnection = new RTCPeerConnection(config)
    peerConnection.onicecandidate = function (event) {
        if (event.candidate) {
            send({
                peer: username,
                event: "candidate",
                data: event.candidate
            });
        }
    };

    dataChannel = peerConnection.createDataChannel("dataChannel", {
        reliable: true
    })

    dataChannel.onerror = function (error) {
        console.log("Error occured on datachannel:", error)
    }

    dataChannel.onmessage = function (event) {
        if (event.data=='pause'){
            video_film.pause()
        }else if (event.data=='play'){
            video_film.play()
        }else{
            data = event.data.split(":")
            if (data[0]=='seeked') {
                currentTime_film = true
                video_film.currentTime = data[1]
                setTimeout(function (){
                    currentTime_film = false
                },100)
            }else if (data[0]=='first_connect'){
                id_call = data[1]
                console.log(My_id,id_call)
            }else if(data[0]=='no_video'){
                let video_call_stream = document.getElementById(data[1])
                raw.removeChild(video_call_stream)
                console.log("del")
            }
            return
        }
        chatLog.value += (event.data + '\n')
    }

    dataChannel.onclose = function () {
        console.log("disconnected")
    }

    peerConnection.ondatachannel = function (event) {
        dataChannel = event.channel
        dataChannel.send('first_connect:' + My_id)
    }
    CreateOffer()
}

function CreateOffer(){
    if (localStream) {
        localStream.getTracks().forEach(track => {
            peerConnection.addTrack(track, localStream)
        })
    }
    peerConnection.createOffer(function (offer) {
        send({
            peer: My_name,
            event: "offer",
            data: offer
        });
        peerConnection.setLocalDescription(offer);
    }, function (error) {
        alert("Error creating an offer");
    })
}

function handleOffer(offer) {
    let remoteStream = new MediaStream();
    add_videoelement(remoteStream,id_call)
    window.stream = remoteStream

    peerConnection.addEventListener('track', async (event) => {
        remoteStream.addTrack(event.track, remoteStream)
    })

    peerConnection.setRemoteDescription(offer)
        .then(() => {
            console.log('Set Remote Description', friend_name);
            return peerConnection.createAnswer()
        })
        .then(answer => {
            console.log('Answer create');
            peerConnection.setLocalDescription(answer)

            send({
                peer: friend_name,
                event: "answer",
                data: answer
            })
        })
}

function handleCandidate(candidate) {
    peerConnection.addIceCandidate(new RTCIceCandidate(candidate));
}

function handleAnswer(answer) {
    remoteStream = new MediaStream()
    add_videoelement(remoteStream,id_call)
    window.stream = remoteStream;

    peerConnection.addEventListener('track', async (event) => {
        remoteStream.addTrack(event.track, remoteStream)
    })

    peerConnection.setRemoteDescription(new RTCSessionDescription(answer))
        .then(() => {
            console.log('Set Remote Description', friend_name)
            return peerConnection.createAnswer()
        })
        .then(answer => {
            console.log('Answer create')
            peerConnection.setLocalDescription(answer)
        })
    console.log("connection established successfully!!")
}

function sendMessage() {
    dataChannel.send(My_name+': '+msg_user.value)
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
            // audioTrack[0].enabled = false
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
        dataChannel.send('no_video:'+My_id)
        
        return
    }

    btn.value = 'off'
    btn.style.background = 'red'
    img_camera.src = camera_img
    my_stream()

    // if (friend_name != My_name) {
    //     initialize(My_name);
    // }
    
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
    dataChannel.send('pause')
})
video_film.addEventListener('play',function(){
    dataChannel.send('play')
})
video_film.addEventListener('seeked',function(){
    if (!currentTime_film) {
        dataChannel.send('seeked:' + video_film.currentTime)
    }
})

video_film.addEventListener('webkitfullscreenchange', function(){
    console.log(video_film.style)
})