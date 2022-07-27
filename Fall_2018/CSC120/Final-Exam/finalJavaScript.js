function navFunction() {
	alert("Zo DiSanto's Final Exam");
}
function myAdd(num1, num2) {
	var x = "17 + 33 = "
    var z = num1 + num2;
	window.alert(x + z);
}
function inputNum() {
	var examGrade = document.getElementById("Exam").value;
	if (examGrade>=65) {
		document.getElementById("examGrade").innerHTML="You passed the class, congrats!!";
	}else if(examGrade<65) {
		document.getElementById("examGrade").innerHTML="You sadly failed the class, try again next semester.";
	}
}
