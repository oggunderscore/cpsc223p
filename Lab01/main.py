"""
NOTE: This program utilizes 'clear' as the clear screen command and is Linux / MacOSX Specific!

Name - Kevin Nguyen
Date - 08/30/23
This file is the main driver of the lab assignment
"""

from contacts import *
import os           # For clearing the screen

contactList = []    # Initialize an empty contact list at program start

userExit = False    # At startup, set to False. This will be set to True when user exits

while (userExit != True):   # Loops while user has not selected exit option
    os.system('clear')
    print('== Main Menu ==\n1 - Print List\n2 - Add Contact\n3 - Modify Contact\n4 - Delete Contact\n5 - Exit')
    
    try:            # Assert that the user will not enter a breaking char
        choice = int(input('> '))
    except Exception as e:
        choice = -1
        
    if choice == 1:
        os.system('clear')
        print_list(contactList)
        input('\nPress enter to continue...')
    elif choice == 2:
        os.system('clear')
        add_contact(contactList)
    elif choice == 3:
        os.system('clear')
        modify_contact(contactList)
    elif choice == 4:
        os.system('clear')
        delete_contact(contactList)
    elif choice == 5:
        print('\nExiting...\n')
        userExit = True
    else: 
        print('\nInput invalid - please try again.')
        input('\nPress enter to continue...')

        
os.system('clear')