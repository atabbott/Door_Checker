from updateDoorStatus import *


# setup a boolean for each door to store the previous state. 
# This way the database will only be updated if a change has occured
leftDoorState = False
rightDoorState = False

# setip a way to exit
nq = True

while nq:
  sateD1 = raw_input("input door 1 state (0 = open, 1 = closed) q to quit");
  sateD2 = raw_input("input door 2 state (0 = open, 1 = closed) q to quit");

  if (sateD1 == "q"):
    nq = False
  else:
    # door 1
    if sateD1 == "1":
      if leftDoorState == False:
        leftDoorState = True
        updateDoorStatus(1,1)
    else:
      if leftDoorState == True:
        leftDoorState = False
        updateDoorStatus(1,1)

    # door 2
    if sateD2 == "1":
      if rightDoorState == False:
        rightDoorState = True
        updateDoorStatus(1,2)
    else:
      if rightDoorState == True:
        rightDoorState = False
        updateDoorStatus(0,2)