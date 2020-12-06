/* Create a new schema for our data */
CREATE SCHEMA `AddressBook` ;

/* Create people_master table
 *   person_id
 *   person_name
 *   person_DOB
 *   active_phone_number
 */
CREATE TABLE `AddressBook`.`people_master` (
  `person_id` INT NOT NULL AUTO_INCREMENT,
  `person_name` VARCHAR(45) NOT NULL,
  `person_DOB` DATE NULL,
  `active_phone_number` VARCHAR(10) NULL,
  PRIMARY KEY (`person_id`),
  UNIQUE INDEX `person_id_UNIQUE` (`person_id` ASC) VISIBLE);

/* Create addresses table
 *   address_id
 *   street_address
 *   city
 *   state
 *   zip_code
 */
CREATE TABLE `AddressBook`.`addresses` (
  `address_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `street_address` VARCHAR(45) NOT NULL,
  `city` VARCHAR(45) NOT NULL,
  `state` VARCHAR(45) NOT NULL,
  `zip_code` VARCHAR(6) NOT NULL,
  PRIMARY KEY (`address_id`));

/* Create people_address table
 *   person_id
 *   address_id
 *   start_date
 *   end_date
 */
CREATE TABLE `AddressBook`.`people_address` (
  `person_id` INT NOT NULL,
  `address_id` INT NOT NULL,
  `start_date` DATE NOT NULL,
  `end_date` DATE NULL;

/* Seed the database with addresses */
INSERT INTO `AddressBook`.`addresses`
  (
    `street_address`,
    `city`,
    `state`,
    `zip_code`
  )
VALUES
  (
    '123 State Street',
    'Anytown',
    'Michigan',
    '11111'
  ),(
    '456 Main Street',
    'Chicago',
    'Illinois',
    '60007'
  ),(
    '89 Another Street',
    'Chicago',
    'Illinois',
    '60007'
  );

/* Seed the database with people */
INSERT INTO `AddressBook`.`people_master`
  (
    `person_name`,
    `person_DOB`,
    `active_phone_number`
  )
VALUES
  (
    'Major',
    '1983-12-08',
    '6161111515'
  ),(
    'Smith',
    '1972-1-22',
    '8881234567'
  ),(
    'Jones',
    '1962-5-14',
    '7771234567'
  ),(
    'DeVries',
    '1982-7-3',
    '9997654323'
  );

/* Seed the database with addresses tied to people */
INSERT INTO `AddressBook`.`people_address`
  (
    `person_id`,
    `address_id`,
    `start_date`,
    `end_date`
  )
VALUES
  (
    '1',
    '1',
    STR_TO_DATE('2000-01-01', '%Y-%m-%d'),
    STR_TO_DATE('2015-03-26', '%Y-%m-%d')
  ),(
    '1',
    '2',
    STR_TO_DATE('2015-03-26', '%Y-%m-%d'),
    NULL
  ),(
    '2',
    '3',
    STR_TO_DATE('2010-05-17', '%Y-%m-%d'),
    NULL
  ),(
    '3',
    '3',
    STR_TO_DATE('2012-02-02', '%Y-%m-%d'),
    NULL
  ),(
    '4',
    '1',
    STR_TO_DATE('2015-03-29', '%Y-%m-%d'),
    NULL
  );
