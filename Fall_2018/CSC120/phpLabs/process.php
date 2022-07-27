<?php
	if($_GET){
		echo'Input from page @ www.myinputPage.com:<br>';
		echo $_GET['fName']."<br>"; 
		echo $_GET['lName"]."<br>";
		echo $_GET['address"]."<br>"; 
	}elseif($_POST){
		echo'Input from the page @ www.POSTForm.com:<br>';
		echo'Input from page @ www.myinputPage.com';
		echo $_GET['fName']."<br>"; 
		echo $_GET['lName"]."<br>";
		echo $_GET['address"]."<br>";
	}

?>