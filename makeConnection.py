#!/usr/bin/env python3

import pymysql

HOST = 'localhost'
USER = 'root'
PASSWORD = 'password'
DB = 'AddressBook'

###################################
# Return a formatted phone number #
###################################
def formatPhone(phone):
  # Slice out Area Code
  areaCodeSlice = slice(3)
  areaCode = phone[areaCodeSlice]

  # Slice out Prefix
  prefixSlice = slice(3, 6)
  prefix = phone[prefixSlice]

  # Slice out Line Number
  lineNumberSlice = slice(6, 10)
  lineNumber = phone[lineNumberSlice]

  # Return formatted number string
  return "({}){}-{}".format(areaCode, prefix, lineNumber)

##########################################
# Print a record using the row's results #
##########################################
def printRecord(row):
  # Format the phone number
  formattedPhone = formatPhone(row['active_phone_number'])

  # Print record for user.
  print("+++++++++++++++++++++++++++++++++++++++++++++++")
  print("++++\n++++    NAME:     ", row['person_name'])
  print("++++\n++++    ADDRESS:  ", row['street_address'])
  print("++++               {}, {} {}".format(row['city'], row['state'], row['zip_code']))
  print("++++\n++++    PHONE:    ", formattedPhone)
  print("++++\n++++    BIRTHDAY: ", row['person_DOB'])
  print("++++               ({} years old)".format(row['age']))
  print("++++\n+++++++++++++++++++++++++++++++++++++++++++++++\n")

#######################################################
# Connect to the database, then execute the statement #
#######################################################
def connectThenExecute(type, statement):
  connection = pymysql.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    db=DB,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
  )

  try:
    # EXECUTE a search by name query
    if type == "basicSelect":
      with connection.cursor() as cursor:
        cursor.execute(statement)
        records = cursor.fetchall()
        if cursor.rowcount > 0:
          for row in records:
            printRecord(row)
        else:
          print("\n++++++++++++++++++++++++++++++++++++++++")
          print("+\n+  No record found.")
          print("+\n++++++++++++++++++++++++++++++++++++++++\n\n")

    # EXECUTE a generic statement
    else:
      with connection.cursor() as cursor:
        cursor.execute(statement)
        records = cursor.fetchall()
        print(records)

  except (connection.Error, connection.Warning) as e:
    print("\n  Something went wrong:\n  {}\n".format(e))

  # Close the connection
  finally:
    connection.close()

def connectAndCount(statement):
  connection = pymysql.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    db=DB,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
  )

  try:
    with connection.cursor() as cursor:
      cursor.execute(statement)
      count = cursor.rowcount
  except (connection.Error, connection.Warning) as e:
    print("\n  Something went wrong:\n  {}\n".format(e))

  # Close the connection
  finally:
    connection.close()
    return count

#######################################################
# Connect to the database, then insert the user       #
#######################################################
def connectThenInsertNew(sqlInsertUser, sqlInsertAddress, sqlMatch):
  connection = pymysql.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    db=DB,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
  )

  try:
    # CREATE a new user
    with connection.cursor() as cursor:
      cursor.execute(sqlInsertUser)
      cursor.execute(sqlInsertAddress)
    connection.commit()

    # Tie together the two new entries
    with connection.cursor() as cursor:
      cursor.execute(sqlMatch)
    connection.commit()

  except (connection.Error, connection.Warning) as e:
    print("\n  Something went wrong:\n  {}\n".format(e))

  # Close the connection
  finally:
    connection.close()

#######################################################
# Connect to the database, then update the user       #
#######################################################
def connectThenUpdatePerson(sqlUpdatePhone, sqlInsertAddress):
  connection = pymysql.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    db=DB,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
  )

  try:
    # CREATE a new user
    with connection.cursor() as cursor:
      cursor.execute(sqlUpdatePhone)
      cursor.execute(sqlInsertAddress)
    connection.commit()

  except (connection.Error, connection.Warning) as e:
    print("\n  Something went wrong:\n  {}\n".format(e))

  # Close the connection
  finally:
    connection.close()
