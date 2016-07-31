from updateDoorStatus import *
from gpiozero import Button

# setup the doors as gpio buttons
leftDoor = Button(2)
rightDoor = Button(17)
# setup a boolean for each door to store the previous state. 
# This way the database will only be updated if a change has occured
leftDoorState = False
rightDoorState = False

while True:
  # door 1
  if leftDoor.is_pressed:
    if leftDoorState == False:
      leftDoorState = True
      updateDoorStatus(1,1)
  else:
    if leftDoorState == True:
      leftDoorState = False
      updateDoor1Status(1,1)

  # door 2
  if rightDoor.is_pressed:
    if rightDoorState == False:
      rightDoorState = True
      updateDoorStatus(1,2)
  else:
    if rightDoorState == True:
      rightDoorState = False
      updateDoorStatus(0,2)