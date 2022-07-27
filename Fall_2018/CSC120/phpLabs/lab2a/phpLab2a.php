<!DOCTYPE html>
<html lang="eng">
<head>
	<title>My Second Part A PHP</title>
<mega charset="utf-8">
</head>
<body>
<h2>Zo DiSanto</h2>
<p>
	~This is my second part A page with PHP in it!
	</p><p>
	This is a PHP loop
	</p>
	<p>
	<?php
	//initialize Counter
	$i=0;
	while($i<150){
		//Increment Counter
		$i++;
		if($i%3){
			continue;
		}
		echo$i.'<br>';
	}
	?>
</p>
</body>
</html>