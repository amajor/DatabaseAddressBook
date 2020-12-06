/* View only current addresses */
SELECT
  people_address.person_id,
  people_address.address_id,
  start_date,
  end_date,
  person_name,
  street_address,
  city,
  state,
  zip_code,
  person_DOB,
  active_phone_number
FROM AddressBook.people_address
JOIN Addressbook.people_master
  ON people_address.person_id = people_master.person_id
JOIN AddressBook.addresses
  ON people_address.address_id = addresses.address_id
WHERE end_date IS NULL;