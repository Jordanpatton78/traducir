var video = document.getElementById("player");
var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");
requestAnimationFrame(draw)

function draw(){
    canvas.width = 300;
    canvas.height = 100;
    ctx.drawImage(video,0,0,300,100);
    imgData = ctx.getImageData(0, 0, canvas.width, canvas.height);
    data = imgData.data;
    for (let i = 0; i < data.length; i += 4) {
        ave = (data[i + 0] + data[i + 1] + data[i + 2]) / 3;
        data[i + 0] =
        data[i + 1] =
        data[i + 2] = (ave > 128) ? 255 : 0;
        data[i + 3] = 255;
        }
        ctx.putImageData(imgData, 0, 0);
    requestAnimationFrame(draw)
}
var snapshotCanvas = document.getElementById('canvas');
var captureButtoneng = document.getElementById('captureeng');
var handleSuccess = function(stream) {
    video.srcObject = stream;
    };
var num = 1;
captureButtoneng.addEventListener('click', function() {
    var context = canvas.getContext('2d');
    context.drawImage(video, 100, 300, 600, 200, 0, 0, snapshotCanvas.width,
        snapshotCanvas.height);
    const url = canvas.toDataURL("image/png");
    Tesseract
        .recognize(url, {
            lang: 'eng'
        })
        .progress(function(p) {
            $("#msg").text(p.status + ": " + p.progress)
        })
        .then(function(result) {
            console.log(result)
            $("#msg").text("Progress Complete.");
            var elem = document.createElement('div');
            elem.innerHTML = "<div id=" + num + " style='width:300px; background-color:#EEEEEE'><img src=" + url + " /></div><br>"
            var parent = document.getElementById("results");
            parent.insertBefore(elem, parent.firstChild);
            var numdiv = document.getElementById(num);
            var msg = document.createElement('div');
            var string = result.text;
            msg.innerHTML = string;
            numdiv.appendChild(msg);
            num += 1;
        });
});
var front = false;
var constraints = {
    audio: false,
    video: {
        width: 1920,
        height: 1080,
        facingMode: (front ? "user" : "environment")
    }
};
navigator.mediaDevices.getUserMedia(constraints).then(handleSuccess);
