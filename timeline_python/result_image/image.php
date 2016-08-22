<!DOCTYPE>
<html>
<head>
</head>

<?php
echo "<h1>Logon Visualization\n</h1>";
$path = ".";
$dh = opendir($path);
$i=1;
?> 


<body>

<?php
echo "Python Version";
while (($file = readdir($dh)) !== false) {
    if($file != "." && $file != ".." && $file != ".git" && $file != "image.html" && $file != "kibana" && $file != "timeline_javascript") {
	echo "<div id=$i>";
	echo "<img src=$file height='840px' width='1280px'>";
	echo "</div>";
        $i++;
    }

}

closedir($dh);
?>

</body>
</html>
