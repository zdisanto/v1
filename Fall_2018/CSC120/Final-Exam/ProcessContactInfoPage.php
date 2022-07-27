<!DOCTYPE html>
<html lang="en">
<head>
<style>

  #theFrom{
position:absolute;
border-style:solid;
left:25%;
top:30%;
width:30%;
background-color:#5F9EA0;
box-shadow: 10px 10px 5px #888888;
padding:10px;
}
</style>
  <title>Processing Contact Info.</title>
  <script src="script.js"></script>
  <link rel="stylesheet" type="text/css" href="finalStyles.css">
  <meta charset="utf-8">
</head>
<body>
<p>Returning from Data</p>
<div id="theForm">
<?php
	$fName = $_POST["fName"];
	$lName = $_POST["lName"];
	$address = $_POST["address"];
	$city = $_POST["city"];
	$state = $_POST["state"];
	$zip = $_POST["zip"];
	$phone = $_POST["phone"];
  $brithday = $_POST["birthday"];
	echo "Hello, ".$fName;
	echo " ".$lName."<br>";
	echo "You live at ".$address;
  echo " ".$city;
	echo " ".$state;
	echo "   ".$zip."<br>";
	echo "Your phone number is: ".$phone."<br>";
  echo "Your birthday is: ".$birthday."<br>";
?>

<footer>
    <small><i>Copyright &copy; 2018 Zo DiSanto</i></small>
</footer>

</body>
</html>
