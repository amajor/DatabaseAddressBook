#!/usr/bin/env python3

import pymysql

def connectThenExecute(type, statement):
  connection = pymysql.connect(
    host='localhost',
    user='root',
    password='password',
    db='AddressBook',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
  )

  try:
    # CREATE a new user
    if type == "insert":
      with connection.cursor() as cursor:
        # Create a new record
        cursor.execute(statement)
      # Commit to save your changes.
      connection.commit()

    # EXECUTE a statement
    else:
      with connection.cursor() as cursor:
        cursor.execute(statement)
        result = cursor.fetchmany(1)
        print(result)

  # Close the connection
  finally:
    connection.close()
