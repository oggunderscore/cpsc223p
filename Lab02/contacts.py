"""
Name - Kevin Nguyen
Date - 08/30/23
This class contains core functions for the contacts list program.
"""
import time


def print_list(contactList):
    """Prints the contact list provided"""
    if len(contactList) > 0:
        print(f'== Contact List ==\n\n{"Index":5} {"First Name":22} {"Last Name":22}\n')
        for x in range(len(contactList)):
            print(f"{str(x):5} {contactList[x][0]:22} {contactList[x][1]:22}")
    else:
        print("Contact List is empty.")


def add_contact(contactList, firstName, lastName):
    """Adds a contact to the contact list"""

    newContact = [firstName, lastName]
    contactList.append(newContact)
    return contactList


def modify_contact(contactList, index, firstName, lastName):
    """Enters Edit Mode for the List"""

    if index > len(contactList) - 1:
        print("\nFailed to edit contact - invalid index\n")
        time.sleep(1)
        return False

    contactList[index][0] = firstName
    contactList[index][1] = lastName
    return True


def delete_contact(contactList, index):
    """Deletes a contact from the list"""
    if index > len(contactList) - 1:
        print("\nFailed to delete contact - invalid index\n")
        time.sleep(1)
        return False

    del contactList[index]
    print("Successfully deleted.")
    time.sleep(0.5)
    return True


def sort_contacts(contactList, column):
    match column:
        case 0:
            print("Sorting by First Name")
            sortedList = sorted(contactList, key=lambda x: x[0])
        case 1:
            print("Sorting by Last Name")
            sortedList = sorted(contactList, key=lambda x: x[-1])
    contactList = sortedList
    return sortedList
