<?php
	$allstates = "Mississippi Alabama Texas Massachusetts Kansas";
	$statesArray=[];
	$states1 = explode(' ', $allstates);
	$i=0;

	foreach($states1 as $state){
		if (preg_match('/xas$/',$state)){
			$statesArray[$i]=$state;
			echo "The state ending with 'xas' is:" . $state. "<br>";
			$i =$i +1;
		}
	}

	foreach($states1 as $state){
		if (preg_match('/^k.*s/',$state)){
			$statesArray[$i]=$state;
			echo "The state starting with 'k' and ending with 's' is:" .$state."<br>";
			$i=$i+1;
		}
	}

	foreach($states1 as $state){
		if(preg_match('/^M.*s/',$state)){
			$statesArray[$i]=$state;
			echo "The state starting with 'M' and ending with 's' is :" .$state."<br>";
			$i =$i +1;
		}
	}

	foreach($states1 as $state){
		if(preg_match('/a$/', $state)){
			$statesArray[$i]=$state;
			echo "The state ending with 'a' is:" . $state . "<br>";
		}
	}

	foreach($statesArray as $element => $value){
		echo nl2br($value." is in position ".$element.".\n");
	}

?>