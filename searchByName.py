#!/usr/bin/env python3

from makeConnection import connectThenExecute

def searchLastName():
  name = input("Enter Last Name: ")
  print("\nSearching by '{}' . . .".format(name))
  print  # Empty line

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
  connectThenExecute('byName', sql)