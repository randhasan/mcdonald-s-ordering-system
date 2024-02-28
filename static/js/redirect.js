// redirect.js (given)
var timeout = 10000; // 10 seconds
window.setTimeout(sendBackToMainScreen, timeout);

function sendBackToMainScreen() {
    window.location = "http://127.0.0.1:5000";
}