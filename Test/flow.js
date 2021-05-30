let URL = "https://www.google.com/";

const btn = document.getElementsByClassName("btn");

btn.addEventListener("click", function (event) {
	console.log(event);
	location.href(URL);
});
