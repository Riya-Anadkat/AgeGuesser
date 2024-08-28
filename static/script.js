function updateRandomNumber() {
    var randomNumber = Math.floor(Math.random() * 101);
    document.getElementById("random-number").textContent = randomNumber;
}

function getFrame() {
    var video = document.getElementById('video');
    var canvas = document.createElement('canvas');
    var context = canvas.getContext('2d');

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight
    context.drawImage(video, 0, 0, canvas.width, canvas.height)

    var frameData = canvas.toDataURL('image/jpeg')

    fetch('/capture_frame', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                frame: frameData
            })
        })
        .catch(error => console.log(error))
}

navigator.mediaDevices.getUserMedia({
        video: true
    })
    .then(function (stream) {
        var video = document.getElementById('video');
        video.srcObject = stream;
    })
    .catch(function (err) {
        console.error('Error accessing the camera:', err);
    });

// setInterval(getFrame, 3000);
setInterval(updateRandomNumber, 200);
