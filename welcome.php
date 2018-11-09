<?php
session_start();
$time = $_SERVER['REQUEST_TIME'];
$timeout_duration = 10;
if (isset($_SESSION['LAST_ACTIVITY']) && 
   ($time - $_SESSION['LAST_ACTIVITY']) > $timeout_duration) {
    session_unset();
    session_destroy();
	session_start();
	header("Location:login.php");
	exit();
}
else if($_SESSION['LAST_ACTIVITY'])
{
	echo '<h1>WELCOME TO MY WEB PAGE</h1>';
}
else
{
	header("Location:login.php");
}
?>