function transit(id, method) {
	// get form from index.html
	let f = document.forms["form"];
	f.method = method;
	// page URL where you want to go
	f.action =
		"https://twilio-video-handson-webrtc-go-3199-dev.twil.io/video.html";

	// get query
	let query = window.location.search;
	console.log(query);

	// get input value
	let input = document.getElementById(id);
	console.log(input.value);
	f.submit();

	return true;
}
