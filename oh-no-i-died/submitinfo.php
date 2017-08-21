<?php
//Don't touch this... Yet...
//This enters the form data into the database. It's NOT final

//db variables, tweak as needed...
$dbhostname = "localhost";
$dbusername = "root";
$dbpassword = "";
$dbname = "ohnoidied";


//Set up member variables...
$firstname = "";
$lastname = "";
$isdead = "";
$bio = "";

//No touchy, this is used later
$querydata = "";
$userid = "";

//This function sanitizes string data
function sanitize($data) {
	$data = trim($data);
	$data = stripslashes($data);
	$data = htmlspecialchars($data);
	return $data;
}

//Getting data and sanitizing...
$firstname = sanitize($_POST["firstname"]);
$lastname = sanitize($_POST["lastname"]);
//Check if the checkbox is ticked...
if (isset($_POST["isdead"])){
	$isdead = 1;
}
else {
	$isdead = 0;
}
//Note that bio is stored without it's newlines parsed.
//This is so we can feed it back into the form as a value if need be...
$bio = sanitize($_POST["bio"]);

//Even when sanitized nl2br works...
//echo nl2br($bio);

//Connects to database
$dblink = mysqli_connect($dbhostname,$dbusername,$dbpassword,$dbname);
if (!$dblink) {
	echo "Uh oh, db didn't connect...</br></br>";
}
else {
	global $querydata;
	global $userid;
	//Query the database and put all this in!!!
	
	//but first... CHECK IF WE'RE EDITING AN EXISTING USER!!
	if (isset($_POST["userid"]) and $_POST["userid"]!=null) {
		//yeah!
		//set userid for next page
		mysqli_query($dblink,'UPDATE userinfo SET FNAME="'.$firstname.'", LNAME="'.$lastname.'", BIO="'.$bio.'" WHERE USERID='.$_POST["userid"].';');
	}
	else {
		//nah..
		mysqli_query($dblink,'INSERT INTO userinfo (FNAME,LNAME,ISDEAD,BIO) VALUES ("'.$firstname.'","'.$lastname.'",'.$isdead.',"'.$bio.'");');
	}
	//set userid for next page
	$userid = mysqli_insert_id($dblink);
	//This was used to test insertion... Remember to use quotes for strings (chars) in SQL
	//mysqli_query($dblink,'INSERT INTO userinfo (FNAME,LNAME,ISDEAD,BIO) VALUES ("Chad","Warden",0,"I like pstriple.")');
	mysqli_close($dblink);
}



//Redirect using header() to the user's new page!



if (isset($_POST["userid"]) and $_POST["userid"]!=null) {
	header( 'Location: viewuser.php?&userid='.$_POST["userid"]);
}
else {
	header( 'Location: viewuser.php?&userid='.$userid );
}


//Time to get outta here...
die()




?>