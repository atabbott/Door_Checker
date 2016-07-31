<?php

  $conn = new mysqli('localhost', 'USERNAME', 'PASSWORD','DATABASENAME');
  if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }
  $sql = "SELECT door_status FROM door_status WHERE door_id=1";
  $result = $conn->query($sql);


  if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
      echo $row['door_status'];
    }
  }
?>
