#!/usr/bin/env python3
import os
from searchByName import searchExactName
from searchByName import searchPartialName
from searchByPhone import searchPhoneAreaCode
from searchByPhone import searchPhonePrefix
from searchByAge import searchAgeRange
from createUser import createNewContact

# Menu Choices
MENU = '''
===================================
|                                 |
|  1 - Search by Exact Name       |
|  2 - Search by Partial Name     |
|                                 |
|  3 - Search by Phone Area Code  |
|  4 - Search by Phone Prefix     |
|                                 |
|  5 - Search by Age              |
|                                 |
|  6 - Create/Update Contact      |
|                                 |
|  0 - Quit                       |
|                                 |
===================================
'''

# Define the main program that will run.
def main():
  # Clear the terminal screen
  os.system('cls' if os.name == 'nt' else 'clear')

  # Get user input
  print(MENU)
  menuChoice = input("Menu Choice: ")

  while True:
    if menuChoice == "1":
      searchExactName()
    elif menuChoice == "2":
      searchPartialName()
    elif menuChoice == "3":
      searchPhoneAreaCode()
    elif menuChoice == "4":
      searchPhonePrefix()
    elif menuChoice == "5":
      searchAgeRange()
    elif menuChoice == "6":
      createNewContact()
    elif menuChoice == "0":
      quit()
    else:
      print("\n*** Not a valid choice. Please choose from the menu. ***\n\n")

    # Present the menu again to the user.
    print(MENU)
    menuChoice = input("Menu Choice: ")

# Run the main program
main()