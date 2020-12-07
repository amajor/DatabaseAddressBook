#!/usr/bin/env python3

import re
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

def createNewContact():
  print("\n  Input user data below.\n")
  name   = input("    Name:           ")
  street = input("    Street Address: ")
  city = input("    City:           ")
  state = input("    State:          ")

  zip_code = input("    Zip:            ")
  while not re.search('\d{5}', zip_code):
    print("\n  *** Invalid zip code.")
    print("    Please enter 5-digits with no formatting.")
    print("      Example: XXXXX")
    zip_code = input("\n    Zip:            ")

  phone = input("    Phone:          ")
  while not re.search('\d{10}', phone):
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

  # # Build SQl query to search by exact match of name.
  # sql = '''
  #   SELECT
  #     person_name,
  #     street_address,
  #     city,
  #     state,
  #     zip_code,
  #     active_phone_number,
  #     person_DOB,
  #     TIMESTAMPDIFF(YEAR, person_DOB, CURDATE()) AS age
  #   FROM AddressBook.people_address
  #   JOIN Addressbook.people_master
  #     ON people_address.person_id = people_master.person_id
  #   JOIN AddressBook.addresses
  #     ON people_address.address_id = addresses.address_id
  #   WHERE end_date IS NULL
  #     AND TIMESTAMPDIFF(YEAR, person_DOB, CURDATE()) BETWEEN {} AND {};
  # '''.format(minAge, maxAge)

  # # Execute the query
  # connectThenExecute('insert', sql)
