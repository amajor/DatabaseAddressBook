#!/usr/bin/env python3
import os
from searchByName import searchLastName
from searchByPrefix import searchPhonePrefix
from searchByAge import searchAgeRange
from createUser import createNewContact

# Menu Choices
MENU = '''
================================
|                              |
|  1 - Search by Last Name     |
|  2 - Search by Phone Prefix  |
|  3 - Search by Age           |
|                              |
|  4 - Create New Contact      |
|                              |
|  5 - Quit                    |
|                              |
================================
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
      searchLastName()
    elif menuChoice == "2":
      searchPhonePrefix()
    elif menuChoice == "3":
      searchAgeRange()
    elif menuChoice == "4":
      createNewContact()
    elif menuChoice == "5":
      quit()
    else:
      print("*** Not a valid choice. Please choose from the menu. ***\n\n")

    # Present the menu again to the user.
    print(MENU)
    menuChoice = input("Menu Choice: ")

# Run the main program
main()