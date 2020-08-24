function loginFunction() {
	var newDate = new Date();
	var time = newDate.getHours();
	var welcomeGreeting;

	if (time < 12) {
		welcomeGreeting = "Good Morning!";
	} else if (time < 17) {
		welcomeGreeting = "Good Afternoon!";
	} else {
		welcomeGreeting = "Good Evening!";
	}

	document.getElementById('greeting').innerHTML = welcomeGreeting;
}

window.onload = function() {
	loginFunction();
};