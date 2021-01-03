<?php

$name=$_GET["name"];
$mob=$_GET["mob"];
$email=$_GET["email"];
include "db.php";
$mysql->query("insert into students(name,email,mob) values('$name','$email','$mob')");
$mysql->close();

header("Location:P10.php");

?>