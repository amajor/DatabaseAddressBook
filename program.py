#!/usr/bin/env python3
import os

# Menu Choices
MENU = '''
=======================
1 - Search by Last Name
2 - Search by Prefix
3 - Search by Age
4 - Create New Contact
5 - Quit
=======================
'''

# Define the main program that will run.
def main():
  # Clear the terminal screen
  os.system('cls' if os.name == 'nt' else 'clear')

  # Get user input
  print("Type the number for your choice, then press 'ENTER':")
  menuChoice = input(MENU)

  while True:
    print()  # Print a new line for spacing

    if menuChoice == "1":
      searchLastName()
    elif menuChoice == "2":
      searchPrefix()
    elif menuChoice == "3":
      searchAge()
    elif menuChoice == "4":
      createContact()
    elif menuChoice == "5":
      quit()
    else:
      print("Not a valid choice. Please choose from the menu.")

    # Present the menu again to the user.
    print # Empty Line
    menuChoice = input(MENU)

def searchLastName():
  lastName = input("Enter Last Name: ")
  print("Searching by '{}'".format(lastName))
  print  # Empty line

def searchPrefix():
  prefix = input("Enter Prefix: ")
  print("Searching by '{}'".format(prefix))
  print  # Empty line

def searchAge():
  age = input("Enter Age: ")
  print("Searching by age '{}'".format(age))
  print # Empty line

def createContact():
  print("Time to create a contact!")

# Run the main program
main()