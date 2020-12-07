#!/usr/bin/env python3

import pymysql

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
  print("\n++++++++++++++++++++++++++++++++++++++++")
  print("+\n+  NAME:     ", row['person_name'])
  print("+\n+  ADDRESS:  ", row['street_address'])
  print("+             {}, {} {}".format(row['city'], row['state'], row['zip_code']))
  print("+\n+  PHONE:    ", formattedPhone)
  print("+\n+  BIRTHDAY: ", row['person_DOB'])
  print("+             ({} years old)".format(row['age']))
  print("+\n++++++++++++++++++++++++++++++++++++++++\n\n")

#######################################################
# Connect to the database, then execute the statement #
#######################################################
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

    # EXECUTE a search by name query
    elif type == "basicSelect":
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

  except:
    print("something went wrong")

  # Close the connection
  finally:
    connection.close()
