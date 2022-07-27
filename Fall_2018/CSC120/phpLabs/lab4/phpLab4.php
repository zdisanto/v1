<!DOCTYPE html>
<html lang="eng">
<head>
	<title>My Fourth PHP</title>
<mega charset="utf-8">
</head>
<body>
<h2>Zo DiSanto</h2>
<p>
	~This is my fourth page with PHP in it!
	</p><p>
	This is a PHP loop
	</p>
	<p>
	<?php
	//initialize Counter
	$i=0;
	while($i<10){
		//Increment Counter
		$i++;
		if($i==6){
			break;
		}
	}
	?>
</p>
</body>
</html>