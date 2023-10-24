from contacts import Contacts


def main():
    contacts = Contacts()  # Instantiate Contacts with the default filename

    # Break this once user wants to exit
    while True:
        # Print the menu prompt
        print("\t======\tTUFFY TITAN CONTACT MAIN MENU\t======")
        print("1. Add contact")
        print("2. Modify contact")
        print("3. Delete contact")
        print("4. Print contact list")
        print("5. Set contact filename")
        print("6. Exit")

        # User input
        choice = input("Enter your choice: ")

        if choice == "1":
            id = input("Enter phone number: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            result = contacts.add_contact(id, first_name, last_name)

            # Case & Error Handling
            if isinstance(result, str):
                print(result)  # Error message
            else:
                print(f"Added {first_name} to Contact List")

        elif choice == "2":
            id = input("Enter phone number to modify: ")
            first_name = input("Enter new first name: ")
            last_name = input("Enter new last name: ")
            result = contacts.modify_contact(id, first_name, last_name)

            # Case & Error Handling
            if isinstance(result, str):
                print(result)  # Error message
            else:
                print(f"Contact with phone number {id} has been updated")

        elif choice == "3":
            id = input("Enter phone number to delete: ")
            result = contacts.delete_contact(id)

            # Case & Error Handling
            if isinstance(result, str):
                print(result)  # Error message
            else:
                print(f"Removed contact with phone number {id} from Contact List")

        elif choice == "4":
            print("==================== CONTACT LIST ====================")
            print(f"{('Last Name'):20}  {('First Name'):20}  {('Phone'):9}")
            print("====================  ====================  ==========")
            for id, info in contacts.data.items():
                print(f"{info[1]:20}  {info[0]:20}  {id:9}")

        elif choice == "5":
            new_filename = input("Enter the new filename: ")
            contacts = Contacts(new_filename)
            print(f"Contacts data will be loaded from {new_filename}")

        elif choice == "6":
            break  # Exit the program

        else:
            print("Invalid choice. Please choose a valid option (1-6).")


if __name__ == "__main__":
    main()
