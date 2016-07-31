import MySQLdb

# define what to do if a door is open (1 = closed, 0 = open)
def updateDoorStatus(state,door):
  # connect to the database
  db = MySQLdb.connect("localhost","piDoor","1234","garage_door")
  # setup cursor
  cursor = db.cursor()
  try:
    # create the sql query to update the database for the correct state and door
    sql = "UPDATE door_status SET door_status="+str(state)+" WHERE door_id=" + str(door)
    # exectute the sql
    cursor.execute(sql)
    # save the changed
    db.commit()
  except:
    # if this failed recover the data to what it was before the query
    db.rollback()
  # close the connection
  db.close()


