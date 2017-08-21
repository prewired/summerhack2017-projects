<?php
//THIS FILE SETS UP THE DB & TABLES


//db variables, tweak as needed...
$dbhostname = "localhost";
$dbusername = "root";
$dbpassword = "";
$dbname = "ohnoidied";



//Connects to mysql
$dblink = mysqli_connect($dbhostname,$dbusername,$dbpassword);
if (!$dblink) {
	echo "Uh oh, db didn't connect...</br></br>";
}
else {
	//Creates the database...
	mysqli_query($dblink,"CREATE DATABASE ohnoidied");
	//Connects to the database
	mysqli_close($dblink);
	$dblink = mysqli_connect($dbhostname,$dbusername,$dbpassword,$dbname);
	//Sets up the userdata table...
	mysqli_query($dblink, "
	CREATE TABLE userinfo (
	USERID INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	FNAME VARCHAR(20) NOT NULL,
	LNAME VARCHAR(20) NOT NULL,
	ISDEAD BOOL NOT NULL,
	BIO VARCHAR(1000)
	)
	");
	
	
	
	mysqli_close($dblink);
}

?>