#!/usr/bin/env python3

from makeConnection import connectThenExecute

def searchPhonePrefix():
  print("\n(AAA)PPP-LLLL\n")
  print("  Area Code   --> (AAA)")
  print("  Prefix      --> PPP")
  print("  Line Number --> LLLL")
  prefix = input("\nEnter 3-Digit Prefix: ")

  while not prefix.isnumeric():
    print("\n*** Not a valid prefix. ***")
    prefix = input("\n  Enter 3-Digit Prefix: ")

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