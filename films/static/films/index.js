let connectButton = document.querySelector('#connectButton')
let divMsg = document.querySelector('#div_message')
let btnCreateChat = document.querySelector('#btnCreateChat')
let chatLog = document.querySelector('#chat-log')
let acceptDiv = document.querySelector('#acceptDiv')
let msg_user = document.querySelector('#messageInput')
let send_mes_btn = document.querySelector('#sendmesbtn')

let conn;
let peerConnection;
let dataChannel;
let friend_name = My_name

const camera = document.querySelector('#myVideo');

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
            // console.log('event.candidate', event.candidate)
        }
    };

    dataChannel = peerConnection.createDataChannel("dataChannel", {
        reliable: true
    })

    dataChannel.onerror = function (error) {
        console.log("Error occured on datachannel:", error)
    }

    dataChannel.onmessage = function (event) {
        chatLog.value += (event.data + '\n')
    }

    dataChannel.onclose = function () {
        console.log("data channel is closed")
        alert("Your interlocutor has disconnected")
    }

    peerConnection.ondatachannel = function (event) {
        dataChannel = event.channel
    }

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
    localStream.getTracks().forEach(track => {
        peerConnection.addTrack(track, localStream);
    })

    let remoteVideo = document.querySelector('#callVideo')
    remoteVideo.srcObject = remoteStream

    window.stream = remoteStream

    peerConnection.addEventListener('track', async (event) => {
        console.log('Adding track: ', event.track)
        remoteStream.addTrack(event.track, remoteStream)
    })

    remoteVideo.play()

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
    console.log("handleCandidate!!")
}

function handleAnswer(answer) {
    remoteStream = new MediaStream()
    let remoteVideo = document.querySelector('#callVideo')
    remoteVideo.srcObject = remoteStream

    window.stream = remoteStream;

    peerConnection.addEventListener('track', async (event) => {
        console.log('Adding track: ', event.track)
        remoteStream.addTrack(event.track, remoteStream)
    })

    remoteVideo.play()

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

function my_stream(e) {
    navigator.mediaDevices.getUserMedia(constraints)
        .then(stream => {
            localStream = stream
            camera.srcObject = localStream
            camera.muted = true

            let audioTrack = stream.getAudioTracks()
            let videoTrack = stream.getVideoTracks()
            //audioTrack[0].enabled = false
            videoTrack[0].enabled = true

            console.log('stream', stream)
        }).catch(error => {
        console.log('Error media', error)
    })
}

function conn_user(btn){
    friend_name = btn.value
    connect()
}

function turn_camera(btn){
    my_stream(btn)
}