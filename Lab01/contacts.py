"""
Name - Kevin Nguyen
Date - 08/30/23
This class contains core functions for the contacts list program.
"""

def print_list(contactList):
    '''Prints the contact list provided'''
    if (len(contactList) > 0):
        print(f'== Contact List ==\n\n{"Index":5} {"First Name":22} {"Last Name":22}\n')
        for x in range(len(contactList)):
            print(f'{str(x):5} {contactList[x][0]:22} {contactList[x][1]:22}')
    else:
        print('Contact List is empty.')
        
def add_contact(contactList):
    '''Adds a contact to the contact list'''
    print(f'== Add Contact ==\n')
    firstNameInput = input('First Name > ')
    lastNameInput = input('Last Name > ')
    newContact = [firstNameInput, lastNameInput]
    contactList.append(newContact)
    return contactList

def modify_contact(contactList):
    '''Enters Edit Mode for the List'''
    print_list(contactList)
    
    try: 
        index = int(input('Contact index to edit > '))
    except Exception as e:
        input('\nFailed to edit contact - invalid input\n\nPress enter to continue...')
        return contactList
    
    if index > len(contactList)-1:
        input('\nFailed to edit contact - invalid index\n\nPress enter to continue...')
        return contactList
        
    firstNameInput = input('First Name > ')
    lastNameInput = input('Last Name > ')
    contactList[index][0] = firstNameInput
    contactList[index][1] = lastNameInput
    print('Contact Updated.')
    return contactList

def delete_contact(contactList):
    '''Deletes a contact from the list'''
    print_list(contactList)
    
    try: 
        index = int(input('Contact index to delete > '))
    except Exception as e:
        input('\nFailed to delete contact - invalid input\n\nPress enter to continue...')
        return contactList
    if index > len(contactList)-1:
        input('\nFailed to delete contact - invalid index\n\nPress enter to continue...')
        return contactList
    
    del contactList[index]
    print('Successfully deleted.')
    return contactList
