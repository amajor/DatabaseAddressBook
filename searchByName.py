#!/usr/bin/env python3

import os
from makeConnection import connectThenExecute

def searchLastName():
  name = input("\n  Enter Last Name: ")

  # Clear the terminal screen
  os.system('cls' if os.name == 'nt' else 'clear')
  print("\nSearching by '{}'...\n".format(name))

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
      AND LOWER(person_name) = LOWER('{}');
  '''.format(name)

  # Execute the query
  connectThenExecute('basicSelect', sql)