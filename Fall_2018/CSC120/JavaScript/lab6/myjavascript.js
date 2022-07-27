function myFunction(){
	var Age= document.getElementById("Age").value;
	var comeBackIn = 0;
	var tooYoung = "You're too young come back in ";
	var years = " years";
	
	if (Age<18){
		comeBackIn = 18 - Age;
		var reply = tooYoung.concat(comeBackIn, years);
		document.getElementById("reply").innerHTML=(reply);
	}
	else if(Age>=18){
		document.getElementById("reply").innerHTML=("Go Out and Vote!");
	}
}

