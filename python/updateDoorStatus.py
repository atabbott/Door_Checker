import MySQLdb

# define what to do if a door is open (1 = closed, 0 = open)
def updateDoorStatus(state,door):
  # connect to the database
  db = MySQLdb.connect("mysql://107.180.26.64","door","1qazxsw2","door")
  # setup cursor
  cursor = db.cursor()
  try:
    # create the sql query to update the database for the correct state and door
    sql = "UPDATE door SET d_state="+str(state)+" WHERE d_id=" + str(door)
    # exectute the sql
    cursor.execute(sql)
    # save the changed
    db.commit()
  except:
    # if this failed recover the data to what it was before the query
    db.rollback()
  # close the connection
  db.close()


