<?php
require_once('functions.php');
?>
<!DOCTYPE html>

<html>
<head>
  <title>Garage Door Status</title>
  <link rel="stylesheet" type="text/css" href="stylesheet.css">
</head>

<body>
  <img src="images/refresh.png" height="20pc" width="20pc" alt="refresh" <button type="Button" name="refresh" onclick="javascript:history.go(0)">
  <table>
    <tr>
      <td>
        <p>left</p>
      </td>
      <td>
        <p>right</p>
      </td>
    </tr>
    <tr>
      <td>
        <?php testDoor1(); ?>
      </td>
      <td>
        <?php testDoor2(); ?>
      </td>
    </tr>
  </table>
</body>
</html>
