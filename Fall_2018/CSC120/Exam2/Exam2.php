<!DOCTYPE html>
<html langu="eng">
<head>
<title>PHP Forms</title>
<link rel="stylesheet" type="text/css" href="styles.css">
<mega charset="utf-8">
</head>

<body>
<h2>Exam 2 Practical</h2>
<p>Zo DiSanto's Exam 2</p>

<form id="formData" name="formData" action="ReturnPage.php" method="POST">
<legend>Account Info:</legend>
<ul>	
	<li><label for="fName"><span id="rqd">*</span>First Name:</label>
	<input type="text" name="fName" class="tb" id="fName" placeholder="First Name" pattern="[A-Za-z]+" required/></li>
	<li><label for="lName"><span id="rqd">*</span>Last Name:</label>
	<input type="text" name="lName" class="tb" id="lName" placeholder="Last Name" pattern="[A-Za-z]+" required/></li>
	<li><label for="email">Email:</label>
	<input type="email" name="email" class="tb" id="email" placeholder="Email"/></li>
	<li><label for="city"><span id="rqd">*</span>City:</label>
	<input type="text" name="city" class="tb" id="city" placeholder="City" pattern="[A-Za-z]+" required/></li>
	<li><label for="state"><span id="rqd">*</span>State:</label>
	<input type="text" name="state" class="tb" id="state" placeholder="Two Capital Letters" pattern="[A-Z]{2}" required/></li>
	<li><label for="zip"><span id="rqd">*</span>Zip:</label>
	<input type="text" name="zip" class="tb" id="zip" placeholder="Five Numbers" pattern="(\d{5}([\-]\d{4})?)" required/></li>
	<li><label for="phone"><span id="rqd">*</span>Phone Number:</label>
	<input type="text" name="phone" class="tb" id="phone" placeholder="Phone Number" pattern="(\d{3}[\-]\d{3}[\-]\d{4})" required/></li>	


<li><input type="submit" value="Submit"></li><br/>
	<li><span id="rqd">*</span>Indicates Required.</li>
</ul>
</form>
</body>
</html>
