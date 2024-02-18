
const capture_btn = document.getElementById('capture_btn');
const image_container = document.getElementById('image_container');
let video = document.getElementById('video');
if (navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: true }).then((strean) => {
        video.srcObject = strean
        console.log("working")
        video.onplay();
        const { height, width } = strean.getTracks()[0].getSettings()
        capture_btn.addEventListener('click', function () {
            capture_btn.classList.add('d-none')
            const track = strean.getVideoTracks()[0]
            const imageCapture = new ImageCapture(track)
            imageCapture.takePhoto().then((blob) => {
                const image = new Image(width, height)
                image.src = URL.createObjectURL(blob)
                image_container.append(image)
            })
        })

    })
}