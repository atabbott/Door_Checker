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
      print("door one closed")
  else:
    if leftDoorState == True:
      leftDoorState = False
      print("door one opened")

  # door 2
  if rightDoor.is_pressed:
    if rightDoorState == False:
      rightDoorState = True
      print("door two closed")
  else:
    if rightDoorState == True:
      rightDoorState = False
      print("door two opened")