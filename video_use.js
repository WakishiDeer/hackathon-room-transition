navigator.getUserMedia =
	navigator.getUserMedia ||
	navigator.webkitGetUserMedia ||
	window.navigator.mozGetUserMedia;
window.URL = window.URL || window.webkitURL;
let video = document.getElementsByClassName("_video");
let localStream = null;
navigator.getUserMedia(
	{ video: true, audio: false },
	function (stream) {
		// for success case
		console.log(stream);
		video.srcObject = stream;
	},
	function (err) {
		// for error case
		console.log(err);
	}
);
