import json


class Contacts:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.data = {}

        try:
            with open(self.filename, "r") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            pass

    def add_contact(self, id=None, first_name=None, last_name=None):
        id = str(id)  # Safe Assertion Check
        if id in self.data:
            return "Error: Contact with this ID already exists."

        self.data[id] = [first_name, last_name]
        self._save_data()  # Sort then save the data
        return {id: self.data[id]}

    def modify_contact(self, id=None, first_name=None, last_name=None):
        id = str(id)  # Safe Assertion Check
        if id not in self.data:
            return "Error: Contact with this ID does not exist."

        self.data[id] = [first_name, last_name]
        self._save_data()  # Sort then save the data
        return {id: self.data[id]}

    def delete_contact(self, id=None):
        id = str(id)  # Safe Assertion Check
        if id not in self.data:
            return "Error: Contact with this ID does not exist."

        deleted_contact = {id: self.data.pop(id)}
        self._save_data()  # Sort then save the data
        return deleted_contact

    def _save_data(self):
        sorted_data = dict(  # Sorted by last then first
            sorted(
                self.data.items(),
                key=lambda item: (item[1][1].lower(), item[1][0].lower()),
            )
        )
        with open(self.filename, "w") as file:
            json.dump(sorted_data, file, indent=4)
