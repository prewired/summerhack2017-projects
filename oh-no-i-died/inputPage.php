<html>
	<head>
		<link rel = "stylesheet" type = "text/css" href = "stylesheet1.css"/>
		<title>
			Input Page
		</title>
	</head>
	<body>
		<div id = "container">
			<div id = "header">
				<header>
					<h2>
						Create a Memorial
					</h2>
					<p style = "border-left:10px solid #00CED1; background-color:008B8B">
						Here you can create yourself a memorial to be seen by future generations.
					</p>
				</header>
			</div>
<?php
//This php is to check if the user wants to edit a profile
//If userid in _POST (actually just use _GET....) is set, edit that user's info!
//Not sure how to pass along to the submit page that I want to edit an existing user's page though...
//Maybe through manually setting a _POST variable in php?
//Would that work?
//EDIT: NOPE, Use a hidden form input. Insecure but it'll work.



//db variables, tweak as needed...
$dbhostname = "localhost";
$dbusername = "root";
$dbpassword = "";
$dbname = "ohnoidied";

//No touchy, these are used later
$userinfo = "";


//Set up member variables...
$userid = "";
$firstname = "";
$lastname = "";
$isdead = "";
$bio = "";




if (isset($_GET["userid"]) and $_GET["userid"]!=null) {
	//Connects to database
	$dblink = mysqli_connect($dbhostname,$dbusername,$dbpassword,$dbname);
	if (!$dblink) {
		echo "Uh oh, db didn't connect...</br></br>";
	}
	else {
		//Don't mind me, just declaring globals...
		global $userinfo;
		
		//Get userdata from the database...
		$userinfo = mysqli_query($dblink,"
		SELECT * FROM userinfo WHERE USERID=".$_GET["userid"].";
		");
		$userinfo = mysqli_fetch_row($userinfo);
		mysqli_close($dblink);
	}
}

if ($userinfo!=null) {
	//Set up info variables...
	$userid = $_GET["userid"];
	$firstname = $userinfo[1];
	$lastname = $userinfo[2];
	$isdead = $userinfo[3];
	//note that bio is stored without it's newlines parsed.
	//This is so we can feed it back into the form as a value if need be...
	$bio = $userinfo[4];
	
	//Check if the checkbox is ticked...
	if ($isdead==0) {
		$isdead = "";
	}
	else {
		$isdead = 'checked="on"';
	}
}



?>
			<div id = "body">
				<section style = "width:60%;">
					<form action="submitinfo.php" method="post">
							<input type="hidden" name="userid" value="<?php echo $userid; ?>">
							Are you dead?: <input type="checkbox" name="isdead" <?php echo $isdead; ?>></input>
							</br>
							First Name: <input style = "background-color: #008B8B; color: #F0FFFF; border:2px solid #00CED1" type="text" name="firstname" maxlength="20" value="<?php echo $firstname; ?>"></input>(20 chars max)</br>
							</br>
							Last Name: <input style = "background-color: #008B8B; color: #F0FFFF; border:2px solid #00CED1" type="text" name="lastname" maxlength="20" value="<?php echo $lastname; ?>"></input>(20 chars max)</br>
							</br>
							Bio:</br><textarea style = "background-color: #008B8B; color: #F0FFFF; border:2px solid #00CED1" name="bio" rows="20" cols="60" maxlength="1000"><?php echo $bio; ?></textarea>(1000 chars max)</br>
							</br>
							<input type="submit" value="Submit"/>
							<input type="reset" value="Reset"/>
					</form>
				</section>
			</div>
			<div id = "footer">
				<footer>
					<p> Copyright 2017 © OhNoIDied Inc. </p>
					<p> Contact Email: <a href = "mailto:example@gmail.com"> example@gmail.com </a> </p>
				</footer>
			</div>
		</div>
	</body>
</html>