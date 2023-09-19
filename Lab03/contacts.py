"""
Name - Kevin Nguyen
Date - 08/30/23
This class contains core functions for the contacts list program.
"""
import time


def print_list(contactList):
    """Prints the contact list provided"""
    if len(contactList) > 0:
        print(
            f'================== Contact List ==================\n\n{"Index":7} {"First Name":21} {"Last Name":22}\n======  ====================  ===================='
        )
        for id, name in contactList.items():
            print(f"{str(id):7} {name[0]:21} {name[1]:22}")
    else:
        print("Contact List is empty.")


def add_contact(contactList, id=None, firstName=None, lastName=None):  # Default Args
    """Adds a contact to the contact list"""
    if id in contactList:
        return "Error"
    contactList[id] = [firstName, lastName]
    return contactList


def modify_contact(contactList, id=None, firstName=None, lastName=None):
    """Enters Edit Mode for the List"""

    if id in contactList:
        contactList[id][0] = firstName
        contactList[id][1] = lastName
        return True
    else:
        print("\nFailed to edit contact - invalid id\n")
        time.sleep(1)
        return False


def delete_contact(contactList, id=None):
    """Deletes a contact from the list"""
    if id not in contactList:
        print("\nFailed to delete contact - invalid id\n")
        time.sleep(1)
        return "Error"

    del contactList[id]
    print("Successfully deleted.")
    time.sleep(0.5)
    return True


def sort_contacts(contactList, column=0):
    """Sorts Contacts List by Last name or First Name"""
    # print(contactList.items())
    # TODO: This is not sorting correctly
    match column:
        case 0:
            sorted(contactList.items(), key=lambda x: x[1][0])
        case 1:
            sorted(contactList.items(), key=lambda x: x[1][-1])
    return contactList


def find_contact(contactDict, find=None):
    """Searches the contactDict by their number, first, or last name based on key provided"""
    searchResults = {}

    # Check if find is an integer
    if isinstance(find, int):
        for contact_id, contact_info in contactDict.items():
            if contact_id == find:
                searchResults[contact_id] = contact_info
    elif isinstance(find, str):
        find = (
            find.lower()
        )  # Convert the search string to lowercase for case-insensitive matching
        for contact_id, contact_info in contactDict.items():
            first_name = contact_info[0].lower()
            last_name = contact_info[1].lower()
            if find in first_name or find in last_name:
                searchResults[contact_id] = contact_info

    return searchResults
