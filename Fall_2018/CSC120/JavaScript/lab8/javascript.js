var num1 = "";
var num2 = "";
var Answer = 0;
var mathFunction = "";
function my1Function(){
	num1 += "1";
	document.getElementById("reply").innerHTML += "1";
}
function my2Function(){
	num1 += "2";
	document.getElementById("reply").innerHTML += "2";
}
function my3Function(){
	num1 += "3";
	document.getElementById("reply").innerHTML += "3";
}
function my4Function(){
	num1 += "4";
	document.getElementById("reply").innerHTML += "4";
}
function my5Function(){
	num1 += "5";
	document.getElementById("reply").innerHTML += "5";
}
function my6Function(){
	num1 += "6";
	document.getElementById("reply").innerHTML += "6";
}
function my7Function(){
	num1 += "7";
	document.getElementById("reply").innerHTML += "7";
}
function my8Function(){
	num1 += "8";
	document.getElementById("reply").innerHTML += "8";
}
function my9Function(){
	num1 += "9";
	document.getElementById("reply").innerHTML += "9";
}
function my0Function(){
	num1 += "0";
	document.getElementById("reply").innerHTML += "0";
}
//function mydFunction(){
//	num1 += ".";
//	document.getElementById("reply").innerHTML += ".";
//}
function myAddingFunction(){
	num2 = parseInt(num1);
	num1 = "";
	mathFunction = "A";
	document.getElementById("reply").innerHTML += " + ";
}
function mySubtractingFunction(){
	num2 = parseInt(num1);
	num1 = "";
	mathFunction = "S";
	document.getElementById("reply").innerHTML += " - ";
}
function myMultiplyingFunction(){
	num2 = parseInt(num1);
	num1 = "";
	mathFunction = "M";
	document.getElementById("reply").innerHTML += " x ";
}
function myDividingFunction(){
	num2 = parseInt(num1);
	num1 = "";
	mathFunction = "D";
	document.getElementById("reply").innerHTML += " &#247 ";
}

function myCFunction(){
	num1=0;
	num2=0;
	mathFunction="";
	Answer=0;
	document.getElementById("reply").innerHTML = "";
}

function myEqualFunction(){
	document.getElementById("reply").innerHTML += " = ";
	var newNum = parseInt(num1);
	if (mathFunction=="A"){
	Answer = parseInt(newNum + num2);
	document.getElementById("reply").innerHTML += Answer;
	}else if (mathFunction=="S"){
	Answer = parseInt(num2 - newNum);
	document.getElementById("reply").innerHTML += Answer;
	}else if(mathFunction=="M"){
	Answer = num2 * newNum;
	document.getElementById("reply").innerHTML += Answer;
	}else if(mathFunction=="D"){
	Answer = num2 / newNum;
	document.getElementById("reply").innerHTML += Answer;
	}
}