import rpyc
from constRPYC import * #-

class Client:
  conn = rpyc.connect(SERVER, PORT) # Connect to the server
  print (conn.root.exposed_value())
  conn.root.exposed_append(5)       # Call an exposed operation,
  conn.root.exposed_append(6)       # and append two elements
  print (conn.root.exposed_value())   # Print the result

  print(conn.root.get_days_until_bday('30/06')) # my bday c:
  print(conn.root.is_leap(2026)) # is not leap
  print(conn.root.add_days_to_date('17/05/2025', 10)) # should be 27/05/2025