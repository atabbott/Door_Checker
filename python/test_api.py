from updateDoorStatus import *
import requests

def updateViaApi(state1,state2):
  url = 'http://localhost/garage_door/webpage/api/set_state.php?d1=' + str(state1) +'&d2=' + str(state2)
  response = requests.get(url)


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
      if leftDoorState == 0:
        leftDoorState = 1
        updateViaApi(leftDoorState,rightDoorState)
    else:
      if leftDoorState == 1:
        leftDoorState = 0
        updateViaApi(leftDoorState,rightDoorState)

    # door 2
    if sateD2 == "1":
      if rightDoorState == 0:
        rightDoorState = 1
        updateViaApi(leftDoorState,rightDoorState)
    else:
      if rightDoorState == 1:
        rightDoorState = 0
        updateViaApi(leftDoorState,rightDoorState)