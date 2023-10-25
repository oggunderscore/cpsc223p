class Person:
    def __init__(self, first_name, last_name):
        self.firstname = first_name
        self.lastname = last_name


class Faculty(Person):
    def __init__(self, first_name, last_name, department):
        # Call Person Default Constructor
        super().__init__(first_name, last_name)

        # Initialize Default Vars
        self.department = department


class Student(Person):
    def __init__(self, first_name, last_name):
        # Call Person Default Constructor
        super().__init__(first_name, last_name)

        # Initialize Default Vars
        self.classyear = None
        self.major = None
        self.advisor = None

    # Define Setters
    def set_class(self, class_year):
        self.classyear = class_year

    def set_major(self, major):
        self.major = major

    def set_advisor(self, faculty):
        self.advisor = faculty
