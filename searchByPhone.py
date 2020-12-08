#!/usr/bin/env python3

import os
from makeConnection import connectThenExecute

def searchPhoneAreaCode():
  print("\n(AAA)PPP-LLLL\n")
  print("  Area Code   --> (AAA)")
  print("  Prefix      --> PPP")
  print("  Line Number --> LLLL")
  prefix = input("\nEnter 3-Digit Area Code: ")

  while not prefix.isnumeric():
    print("\n*** Not a valid area code. ***")
    prefix = input("\n  Enter 3-Digit Area Code: ")

  # Clear the terminal screen
  os.system('cls' if os.name == 'nt' else 'clear')
  print("\nSearching by '({})xxx-xxxx'...\n".format(prefix))

  # Build SQl query to search by exact match of name.
  sql = '''
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
      AND active_phone_number LIKE "{}_______";
  '''.format(prefix)

  # Execute the query
  connectThenExecute('basicSelect', sql)

def searchPhonePrefix():
  print("\n(AAA)PPP-LLLL\n")
  print("  Area Code   --> (AAA)")
  print("  Prefix      --> PPP")
  print("  Line Number --> LLLL")
  prefix = input("\nEnter 3-Digit Prefix: ")

  while not prefix.isnumeric():
    print("\n*** Not a valid prefix. ***")
    prefix = input("\n  Enter 3-Digit Prefix: ")

  # Clear the terminal screen
  os.system('cls' if os.name == 'nt' else 'clear')
  print("\nSearching by '(xxx){}-xxxx'...\n".format(prefix))

  # Build SQl query to search by exact match of name.
  sql = '''
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
      AND active_phone_number LIKE "___{}____";
  '''.format(prefix)

  # Execute the query
  connectThenExecute('basicSelect', sql)