"""
NOTE: This program utilizes 'clear' as the clear screen command and is Linux / MacOSX Specific!

Name - Kevin Nguyen
Date - 08/30/23
This file is the main driver of the lab assignment
"""

from contacts import *
import os  # For clearing the screen
import time

contactList = []  # Initialize an empty contact list at program start

userExit = False  # At startup, set to False. This will be set to True when user exits

while userExit != True:  # Loops while user has not selected exit option
    os.system("clear")
    print(
        "== Main Menu ==\n1 - Print List\n2 - Add Contact\n3 - Modify Contact\n4 - Delete Contact\n5 - Exit"
    )

    try:  # Assert that the user will not enter a breaking char
        choice = int(input("> "))
    except Exception as e:
        choice = -1

    if choice == 1:
        os.system("clear")
        print_list(contactList)
        input("\nPress enter to continue...")
    elif choice == 2:
        os.system("clear")
        print(f"== Add Contact ==\n")
        firstNameInput = input("First Name > ")
        lastNameInput = input("Last Name > ")
        add_contact(contactList, firstName=firstNameInput, lastName=lastNameInput)
        print(f"\nSuccessfully added.")
        time.sleep(0.5)
    elif choice == 3:
        os.system("clear")
        print_list(contactList)
        try:
            index = int(input("\nContact index to edit > "))

            firstNameInput = input("First Name > ")
            lastNameInput = input("Last Name > ")

            if modify_contact(
                contactList, index, firstName=firstNameInput, lastName=lastNameInput
            ):
                print("\nContact Updated.")
                time.sleep(0.5)

        except Exception as e:
            print("\nFailed to edit contact - invalid input")
            time.sleep(1)

    elif choice == 4:
        os.system("clear")
        print_list(contactList)

        try:
            index = int(input("Contact index to delete > "))
            delete_contact(contactList, index)
        except Exception as e:
            print("\nFailed to delete contact - invalid input\n")
            time.sleep(1)

    elif choice == 5:
        print("\nExiting...\n")
        time.sleep(0.5)
        userExit = True
    else:
        print("\nInput invalid - please try again.")
        time.sleep(1)


os.system("clear")
