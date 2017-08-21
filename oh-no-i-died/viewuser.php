<!DOCTYPE html>
<?php
//db variables, tweak as needed...
$dbhostname = "localhost";
$dbusername = "root";
$dbpassword = "";
$dbname = "ohnoidied";

//No touchy, these are used later
$userinfo = "";



//Connects to database
$dblink = mysqli_connect($dbhostname,$dbusername,$dbpassword,$dbname);
if (!$dblink) {
	echo "Uh oh, db didn't connect...</br></br>";
}
elseif (isset($_GET["userid"]) and $_GET["userid"]!=null) {
	//Don't mind me, just declaring globals...
	global $userinfo;
	
	//Get userdata from the database...
	$userinfo = mysqli_query($dblink,"
	SELECT * FROM userinfo WHERE USERID=".$_GET["userid"].";
	");
	$userinfo = mysqli_fetch_row($userinfo);
	mysqli_close($dblink);
}
else {
	echo 'No UserID specified!</br></br>';
}


//This function sanitizes string data
function sanitize($data) {
	$data = trim($data);
	$data = stripslashes($data);
	$data = htmlspecialchars($data);
	return $data;
}

//does the user exist?
if ($userinfo!=null) {
	//Set up info variables...
	$firstname = $userinfo[1];
	$lastname = $userinfo[2];
	$isdead = $userinfo[3];
	//note that bio is stored without it's newlines parsed.
	//This is so we can feed it back into the form as a value if need be...
	$bio = $userinfo[4];
	
	//Check if the checkbox is ticked...
	if ($isdead==0) {
		$isdead = "NO";
	}
	else {
		$isdead = "YES";
	}
}
?>
<html> 
	<head>
		<link type = "text/css" rel = "stylesheet" href = "stylesheet1.css"/>
		<title>
			User View Page
		</title>
	<body>
		<div id = "container">
			<div id = "header">
				<header>
					<h2>
						<?php echo"$firstname $lastname" ?>
					</h2>
					<?php if ($isdead=="YES")  {
						echo "<p style = 'border-left:10px solid #00CED1; background-color:008B8B'>
							You are viewing $firstname 's profile. This profile has been archived. We are sorry for your loss.
						</p>";
					}
					?>
				</header>
			</div>
			<div id = "body">
				<section width = "80%">
				<?php echo"
					<h3>
						<u>
							$firstname $lastname 's Bio
						</u>
					</h3>
					<p>
						$bio
					</p>";
				?>
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