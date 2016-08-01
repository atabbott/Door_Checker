from updateDoorStatus import *
from gpiozero import Button
import requests

def updateViaApi(state1,state2):
  url = 'http://localhost/garage_door/webpage/api/set_state.php?d1=' + str(state1) +'&d2=' + str(state2)
  response = requests.get(url)


# setup the doors as gpio buttons
leftDoor = Button(2)
rightDoor = Button(17)
# setup a boolean for each door to store the previous state. 
# This way the database will only be updated if a change has occured
leftDoorState = 0
rightDoorState = 0

while True:
  # door 1
  if leftDoor.is_pressed:
    if leftDoorState == 0:
      leftDoorState = 1
      updateViaApi(leftDoorState,rightDoorState)
  else:
    if leftDoorState == 1:
      leftDoorState = 0
      updateViaApi(leftDoorState,rightDoorState)

  # door 2
  if rightDoor.is_pressed:
    if rightDoorState == 0:
      rightDoorState = 1
      updateViaApi(leftDoorState,rightDoorState)
  else:
    if rightDoorState == 1:
      rightDoorState = 0
      updateViaApi(leftDoorState,rightDoorState)