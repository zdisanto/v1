<!DOCTYPE html>
<html lang="eng">
<head>
	<title>My First PHP</title>
<mega charset="utf-8">
</head>
<body>
<h2>Zo DiSanto</h2>
<p>
	~This is my first page with PHP in it!
	</p><p>
	This is a PHP loop
	</p>
	<p>
	<?php
	//Initialize counter.
	$i=0;

	while ($i<14){
		//increment our counter
		$i++;
		echo$i.'<br>';
	}
	?>
</p>
</body>
</html>