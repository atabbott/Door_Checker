<?php

function connect(){
  $conn = new mysqli('localhost', 'piDoor', '1234','garage_door');
  if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }
  return $conn;
}

function testDoor1(){
  $conn = connect();
  $sql = "SELECT door_status FROM door_status WHERE door_id=1";
  $result = $conn->query($sql);
  if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
      if ($row['door_status'] == 1){
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

function testDoor2(){
  $conn = connect();
  $sql = "SELECT door_status FROM door_status WHERE door_id=2";
  $result = $conn->query($sql);
  if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
      if ($row['door_status'] == 1){
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
