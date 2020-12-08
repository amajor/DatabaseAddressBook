#!/usr/bin/env python3

import re
from makeConnection import connectAndCount
from makeConnection import connectThenUpdatePerson
from makeConnection import connectThenInsertNew
from makeConnection import connectThenExecute

def validateDate(string):
  isValid = True

  # Does it match the expected format YYYY-mm-dd?
  matchFormat = re.search(r"\d{4}-\d{1,2}-\d{1,2}", string)
  if not matchFormat:
    print("\n  *** Does not match format: YYYY-mm-dd")
    isValid = False
    return isValid

  splitDate = string.split("-")

  # Validate the month
  month = splitDate[1]
  isValid = int(month) <= 12
  if not isValid:
    print("\n  *** {} is not a real month.".format(month))
    return isValid

  # Validate the day
  day = splitDate[2]
  # TODAY: We can get more complex here based on the month.
  isValid = int(day) <= 31
  if not isValid:
    print("\n  *** {} is not a real day of the month.".format(day))
    return isValid

  # return results
  return isValid

def checkIfUserExists(name):
  # Build SQl query to search by exact match of name.
  sql = '''
    SELECT person_name FROM Addressbook.people_master
      WHERE LOWER(person_name) = LOWER('{}');
  '''.format(name)

  # Execute the query
  count = connectAndCount(sql)
  if count > 0:
    return True
  else:
    return False

def displayUserContact(name):
  # Display newly added user
  sqlNewUser = '''
    SELECT
      person_name,
      street_address,
      city,
      state,
      zip_code,
      active_phone_number,
      person_DOB,
      TIMESTAMPDIFF(YEAR, person_DOB, CURDATE()) AS age
    FROM AddressBook.people_address
    JOIN Addressbook.people_master
      ON people_address.person_id = people_master.person_id
    JOIN AddressBook.addresses
      ON people_address.address_id = addresses.address_id
    WHERE end_date IS NULL
      AND LOWER(person_name) = LOWER('{}');
  '''.format(name)

  # Execute the query
  connectThenExecute('basicSelect', sqlNewUser)

def createNewContact():
  print("\n  Input user data below.\n")
  name   = input("    Name:           ")
  street = input("    Street Address: ")
  city = input("    City:           ")
  state = input("    State:          ")

  zip_code = input("    Zip:            ")
  while not re.search(r'\d{5}', zip_code):
    print("\n  *** Invalid zip code.")
    print("    Please enter 5-digits with no formatting.")
    print("      Example: XXXXX")
    zip_code = input("\n    Zip:            ")

  phone = input("    Phone:          ")
  while not re.search(r'\d{10}', phone):
    print("\n  *** Invalid phone number.")
    print("    Please enter 10-digits with no formatting.")
    print("      Example: XXXXXXXXXX")
    phone = input("\n    Phone:          ")

  dateOfBirth = input("    Birthday:       ")
  isValid = validateDate(dateOfBirth)
  while not isValid:
    print("    Please enter in the format YYYY-MM-DD.")
    print("      Example: 1985-12-3 or 2010-1-13")
    dateOfBirth = input("\n    Birthday:       ")
    isValid = validateDate(dateOfBirth)

  userExists = checkIfUserExists(name)
  if userExists:
    print("\nuser exists!")
    sqlUpdatePhone = '''
      UPDATE AddressBook.people_master
      SET
        active_phone_number = '{1}'
      WHERE LOWER(person_name) = LOWER('{0}');
    '''.format(name, phone)
    connectThenUpdatePerson(sqlUpdatePhone)
    displayUserContact(name)

  else:
    sqlInsertUser = '''
      INSERT INTO `AddressBook`.`people_master` (
        `person_name`,
        `person_DOB`,
        `active_phone_number`
      ) VALUES (
        '{0}',
        '{1}',
        '{2}'
      );
    '''.format(name, dateOfBirth, phone)
    sqlInsertAddress = '''
      INSERT INTO `AddressBook`.`addresses` (
        `street_address`,
        `city`,
        `state`,
        `zip_code`
      ) VALUES (
        '{0}',
        '{1}',
        '{2}',
        '{3}'
      );
    '''.format(street, city, state, zip_code)
    sqlMatch = '''
      INSERT INTO `AddressBook`.`people_address` (
        `person_id`,
        `address_id`,
        `start_date`
      ) VALUES (
        (
        -- Select the auto-generated id for the person just created.
        SELECT person_id FROM `AddressBook`.`people_master`
          WHERE person_name = '{0}'
          AND person_DOB = '{1}'
          AND active_phone_number = '{2}'
        ),
        (
        -- Select the auto-generated id for the address just created.
        SELECT address_id FROM `AddressBook`.`addresses`
          WHERE street_address = '{3}'
          AND city = '{4}'
          AND state = '{5}'
          AND zip_code = '{6}'
        ),
        CURDATE()
      );
    '''.format(name, dateOfBirth, phone, street, city, state, zip_code)

    # Execute the query
    connectThenInsertNew(sqlInsertUser, sqlInsertAddress, sqlMatch)
    print("\nSuccessfully added {}!\n".format(name))

    # Display newly added user
    displayUserContact(name)
