var secretNum = Math.round(Math.random()*100)+1;
var guessCount = 0;

function Yes() {
	document.getElementById("inputArea").style.display = "block";
}
function No(){
		var n = insulting();
	if(guessCount>0){
		document.getElementById("startingBoard").style.display = "none";
	}
}
function guess(){
	numGuess = numGuess + 1;
	var guess = document.getElementById("guess").value;
		if(playerGuess>secretNum){
			document.getElementById("reply").innerHTML = "Your guess was too high! You have used " + guessCount + " guesses.";
			document.getElementById("guess").value="";
			document.getElementById("guess").focus;
		}else if(guess<secretNum){
			document.getElementById("reply").innerHTML = "Your guess was too low! You have used " + guessCount + " guesses.";
			document.getElementById("guess").value="";
			document.getElementById("guess").focus;
		}else if(guess==secretNum){
			document.getElementById("reply").innerHTML = "You guessed it! You have used " + guessCount + " guesses.";
			document.getElementById("guess").value="";
			document.getElementById("guess").focus;
		}
}