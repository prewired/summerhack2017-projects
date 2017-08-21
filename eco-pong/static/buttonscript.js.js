
var player1 = "P1_38";
function player1ButtonClick(id) {
	console.log(id);
	console.log(player1);
	document.getElementById(id).classList.add('selected_button');
	document.getElementById(id).classList.remove('selection_button');
	document.getElementById(player1).classList.add('selection_button');
	document.getElementById(player1).classList.remove('selected_button');
	player1 = id;
	return;
}

var player2 = "P2_38";
function player2ButtonClick(id) {
	document.getElementById(id).classList.add('selected_button');
	document.getElementById(id).classList.remove('selection_button');
	document.getElementById(player2).classList.add('selection_button');
	document.getElementById(player2).classList.remove('selected_button');
	player2 = id;
	return;
}
