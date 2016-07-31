<?php

function connect(){
  require_once('connection_settings.php');
  $conn = new mysqli($hostname, $username, $pwd,$db);
  if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }
  return $conn;
}

function testDoor(door){
  $conn = connect();
  $sql = "SELECT door_status FROM door_status WHERE door_id=".str($door);
  $result = $conn->query($sql);
  if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
      if ($row['door_status'] == 0){
        echo "<img src='images/open.jpg' alt='OPEN' height='100pc' width='100pc'/>";
        echo "<p>OPEN</p>";
      }
      else{
        echo "<img src='images/closed.jpg' alt='closed' height='100pc' width='100pc'/>";
        echo "<p>closed</p>";
      }
    }
  }
  $result->free();
}



?>
