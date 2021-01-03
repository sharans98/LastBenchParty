<!DOCTYPE html>
<html>
<head>
	<title>Matrix Operations</title>
	<style>
	</style>
</head>
<body>
<?php
	$m1=array(array(4,5),array(6,7));
	$m2=array(array(1,0),array(0,1));
	echo "The order of matrix A is " . count($m1) . "x" . count($m1[0]);
	echo "The order of matrix B is " . count($m2) . "x" . count($m2[0]);
	$rowcount=count($m1);
	$colcount=count($m1[0]);
	echo nl2br ("The Matrix A is : \n");
	for($rc=0;$rc<$rowcount;$rc+=1){
		for($cc=0;$cc<$colcount;$cc+=1){
			echo nl2br ($m1[$rc][$cc] . "\t");
		}
		echo nl2br ("\n");
	}
	echo nl2br ("The Matrix B is : \n");
	for($rc=0;$rc<$rowcount;$rc+=1){
		for($cc=0;$cc<$colcount;$cc+=1){
			echo nl2br ($m2[$rc][$cc] . "");
		}
		echo nl2br ("\n");
	}

	echo nl2br ("The Transpose Matrix A is : \n");
	for($rc=0;$rc<$rowcount;$rc+=1){
		for($cc=0;$cc<$colcount;$cc+=1){
			echo nl2br ($m1[$cc][$rc] . "\t");
		}
		echo nl2br ("\n");
	}

	echo nl2br ("The Matrix Addition is : \n");
	for($rc=0;$rc<$rowcount;$rc+=1){
		for($cc=0;$cc<$colcount;$cc+=1){
			$val=$m1[$rc][$cc] + $m2[$rc][$cc];
			echo nl2br ($val . "\t");
		}
		echo nl2br ("\n");
	}

	echo nl2br ("The Matrix Multiplication is : \n");
	for($rc=0;$rc<$rowcount;$rc+=1){
		for($cc=0;$cc<$colcount;$cc+=1){
			$val = 0;
			for ($i=0;$i<$rowcount;$i+=1){
				$val += $m1[$rc][$i]*$m2[$i][$cc];
			}
				echo nl2br ($val . "\t");
		}
		echo nl2br ("\n");
	}


?>
</body>
</html>