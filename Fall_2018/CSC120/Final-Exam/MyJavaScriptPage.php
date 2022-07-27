<!DOCTYPE html>
<html lang="en">
<head>
<title>Final Exam</title>
<script src="finalJavaScript.js"></script>
<link rel="stylesheet" type="text/css" href="finalStyles.css">
<meta charset="utf-8">
</head>
<body>
<script>
window.alert("Zo DiSanto's Final Exam");
</script>
<header>
  <h1>Zo DiSanto's Final Exam</h1>
</header>
<nav>
  <ul>
     <li><a href="index.php">Home Page</a></li>
     <li><a href="MyJavaScriptPage.php">JavaScript Page</a></li>
     <li><a href="ContactPage.php">Contact Page</a></li>
  </ul>
</nav>

<p>
Click below for simple math...<br/>
<input type="button" value="Click Me!" onclick="myAdd(17,33)"/><br/>
<br/>
</p>
<p>
Input Exam grade: <br/>
<input type="number" id="Exam" label = "Exam Grade"></input><br/>
<button type="button" onclick="inputNum()">Results</button>
</p>
<p id = "examGrade"></p>

<footer>
  <small><i>Copyright &copy; 2018 Zo DiSanto</i></small>
</footer>

</body>
</html>
