<!DOCTYPE html>
<html>
<head>
	<title>Students</title>
</head>
<body>
	<form action="store.php" method="GET">
		<h2>Enter Student Details</h2>
		<label>Name:</label>
		<input type="text" name="name"/><br>
		<label>Email:</label>
		<input type="type" name="email"/><br>
		<label>Mobile:</label>
		<input type="number" name="mob"/><br>
		<input type="submit" value="Store Details"/>
	</form>

	<?php
		include "db.php";
		$result=$mysql->query("select * from students;");
		while($row = $result->fetch_array()){
			$stu[] = array('name'=> $row[0], 'email'=> $row[1], 'mob'=>$row[2]);
		}
	?>
	<hr>
	<h3>The list of sorted students are:</h3><br>
	<table border="1">
		<tr>
			<th>Name</th>
			<th>Email</th>
			<th>Mobile</th>
		</tr>


	<?php
		$fin=selection_sort($stu);
		for($i=0;$i<count($fin);$i=$i+1){
			echo "<tr><td>" . $fin[$i]['name'] . "</td><td>" .$fin[$i]['email'] . "</td><td>" .$fin[$i]['mob'] . "</td></tr>";
		}
		
		function selection_sort($data){
			$count=count($data);
			for ($i=0;$i<$count-1;$i=$i+1){
				$min=$i;
				for($j=$i+1;$j<$count;$j=$j+1) {
					if(strcmp(strtolower($data[$j]['name']),strtolower($data[$min]['name']))<0){
						$min=$j;
					}
				}
				$temp=$data[$min];
				$data[$min]=$data[$i];
				$data[$i]=$temp;
			}
			return $data;
		}
	?>

</body>
</html>