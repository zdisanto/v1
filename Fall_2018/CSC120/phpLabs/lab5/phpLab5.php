<?php
$cities=['Syracuse','Buffalo','Rochester','Albany','NYC'];
?>
<!DOCTYPE html>
<html lang="eng">
<head>
	<title>My Fifth PHP</title>
<mega charset="utf-8">
</head>
<body>
<h2>Cities in NY State</h2>
<p>
	This list is generated using a for loop
	</p>
	<ul>
	<?php
	$num_items=count($cities);
	for($i=0;$i<num_items;$i++){
		echo"<li>$cities[$i]</li>";
	}
	?>
</ul>
</body>
</html>