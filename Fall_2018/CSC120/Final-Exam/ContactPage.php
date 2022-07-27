<!DOCTYPE html>
<html lang="en">
<head>
<title>Final Exam</title>
<meta charset="utf-8">
<link rel="stylesheet" type="text/css" href="finalStyles.css">
<script src="finalJavaScript.js"></script>
</head>
<body>
<header>
  <h1>Zo DiSanto's Final Exam</h1>
  <style>
	#myForm{
	position:absolute;
	border-style:solid;
	left:5%;
	top:20%;
	width:30%;
	background-color:#BEBEBE;
	box-shadow:10px 10px 5px #888888;
	padding:10px;
	}
	.tb{
	position:absolute;
	left:40%;
	}

	li{
	margin:5px;
	}
	ul{
	list-style:none;
	}

	#rqd{
	color:red;
	}
  </style>
</header>
<nav>
  <ul>
     <li><a href="index.php">Home</a></li>
     <li><a href="MyJavaScriptPage.php" onclick="msg()">MyJavaScriptPage</a></li>
	 <li><a href="ContactPage.php">ContactPage</a></li>
  </ul>
</nav>
<main>

<form id="myForm" name="TheForm" class="group" action="ProcessContactInfoPage.php" method="POST">
<legend>Contact Info</legend>
<ul>
<li><label for="fName"><span id="rqd">*</span>First Name</label>
<input type="text" name="fName" class="tb" id="fName" placeholder="First Name" pattern="[A-Za-z]+" maxlength="5" required /></li><br>
<li><label for="lName"><span id="rqd">*</span>Last Name</label>
<input type="text" name="lName" class="tb" id="lName" placeholder="Last Name" pattern="[A-Za-z]+" maxlength="10" required /></li><br>
<li><label for="address"><span id="rqd">*</span>Address</label>
<input type="text" name="address" class="tb" id="address" placeholder="Address" maxlength="15" required /></li><br>
<li><label for="city"><span id="rqd">*</span>City</label>
<input type="text" name="city" class="tb" id="city" placeholder="City" pattern="[A-Za-z]+" required /></li><br>
<li><label for="state"><span id="rqd">*</span>State</label>
<input type="text" name="state" class="tb" id="state" placeholder="2 Letter State Abrvtn" pattern="[A-Z]{2}" required /></li><br>
<li><label for="zip"><span id="rqd">*</span>Zip Code</label>
<input type="text" name="zip" class="tb" id="zip" placeholder="Zip Code" pattern="(\d{5}([\-]\d{4})?)" required /></li><br>
<li><label for="phone"><span id="rqd">*</span>Phone Number</label>
<input type="text" name="phone" class="tb" id="phone" placeholder="Phone Number" pattern="(\d{3})(\d{3})(\d{4})" required /></li><br>
<li><label for="birthday"><span id="rqd">*</span>Birthday</label>
<input type="date" name="birthday" class="tb" id="birthday" placeholder="Birthday" required /></li><br>

<button type="submit">Submit</button><br>
<li><label for="require"><span id="rqd">*</span>Indicates required</label></li>
</ul>
</form>

</main>

<footer>
    <small><i>Copyright &copy; 2018 Zo DiSanto</i></small>
</footer>

</body>
</html>
