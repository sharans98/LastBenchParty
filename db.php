<?php

$mysql = new mysqli("localhost" , "root" , "" , "db10");
if (mysqli_connect_errno()){
	echo "Database Connection error!";
	exit();
}
?>