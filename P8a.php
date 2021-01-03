<!DOCTYPE html>
<html>
<head>
	<title>Simple Calculator Using PHP</title>
	<style>
	</style>
</head>
<body>
	<h1>Simple Calculator using PHP</h1>
	<hr>
	<form action="P8a.php" method="POST">
	<label>Enter first number:</label>
	<input type="number" name="n1" id="n1" required />
	<label>Enter second number:</label>
	<input type="number" name="n2" id="n2" required />
	<label>Select operation:</label>
	<select name="op">
		<option value="+">Addition</option>
		<option value="-">Subtraction</option>
		<option value="*">Multiplication</option>
		<option value="/">Division</option>
		<option value="%">Remainder</option>
	</select>
	<input type="submit" id="res" name="res" value="Perform Operation">
	</form>
<?php
	if(isset($_POST["res"])){
		$n1=$_POST["n1"];
		$n2=$_POST["n2"];
		$op=$_POST["op"];
		$result=0;
		switch($op){
			case '+' : $result = $n1+$n2;
				echo "The addition of two numbers is " . $result;
				break;
			case '-' : $result = $n1-$n2;
				echo "The difference of two numbers is " . $result;
				break;
			case '*' : $result = $n1*$n2;
				echo "The product of two numbers is " . $result;
				break;
			case '/' : $result = $n1/$n2;
				echo "The quotient of two numbers is " . $result;
				break;
			case '%' : $result = $n1%$n2;
				echo "The remainder after division of two numbers is " . $result;
				break;
			
		}
	}
?>


</body>
</html>
