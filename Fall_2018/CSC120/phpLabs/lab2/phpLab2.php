<!DOCTYPE html>
<html lang="eng">
<head>
	<title>My Second PHP</title>
<mega charset="utf-8">
</head>
<body>
<h2>Zo DiSanto</h2>
<p>
	~This is my second page with PHP in it!
	</p><p>
	This is a PHP loop
	</p>
	<p>
	<?php
	//initialize Counter
	$i=100;
	do{
		//Increment Counter
		$i++;
		echo$i.'<br>';
	}while($i<10);
	?>
</p>
</body>
</html>