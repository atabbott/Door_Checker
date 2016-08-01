<?php
  require_once('../functions.php');

  //check the inputs from get
  function checkInputs(){
    if (!empty($_GET['d1']) & !empty($_GET['d2']){
      return True;
    }
    else {
      return False;
    }
  }

checkInputs();
updateDoorState(1,$_GET['d1']);
updateDoorState(2,$_GET['d2']);
?>
