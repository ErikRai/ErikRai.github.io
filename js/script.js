var style = `
button {
    display: none;
}
`
var styleSheet = document.createElement("style")
styleSheet.type = "text/css"
styleSheet.innerText = style

var elem = document.documentElement;
function openFullscreen() {
if (elem.requestFullscreen) {
elem.requestFullscreen();
elem.appendChild(styleSheet);
} else if (elem.mozRequestFullScreen) { /* Firefox */
elem.mozRequestFullScreen();
elem.appendChild(styleSheet);
} else if (elem.webkitRequestFullscreen) { /* Chrome, Safari & Opera */
elem.webkitRequestFullscreen();
elem.appendChild(styleSheet);
} else if (elem.msRequestFullscreen) { /* IE/Edge */
elem.msRequestFullscreen();
elem.appendChild(styleSheet);
}
if (document.exitFullscreen) {
document.exitFullscreen();
} else if (document.mozCancelFullScreen) {
document.mozCancelFullScreen();
} else if (document.webkitExitFullscreen) {
document.webkitExitFullscreen();
} else if (document.msExitFullscreen) {
document.msExitFullscreen();
}
}