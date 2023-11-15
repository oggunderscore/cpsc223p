class Person:
    def __init__(self, first_name, last_name, gender, age):
        self.firstname = first_name
        self.lastname = last_name
        self.gender = gender
        self.age = age

    def getName(self):
        return f"{self.firstname} {self.lastname}"


class Student(Person):
    def __init__(self, first_name, last_name, gender, age, id):
        # Call Person Default Constructor
        super().__init__(first_name, last_name, gender, age)

        # Initialize Default Vars
        self.id = id

    def getName(self):
        return f"{self.firstname} {self.lastname} | ID: {self.id}"


class StudentAthlete(Student):
    instanceCount = 0

    def __init__(self, first_name, last_name, gender, age, id, sport):
        # Call Person Default Constructor
        super().__init__(first_name, last_name, gender, age, id)

        # Initialize Default Vars
        self.sport = sport
        StudentAthlete.instanceCount += 1

    def getSport(self):
        return self.sport


def main():
    x = Person("Jose", "Cruz", "Male", 45)
    y = StudentAthlete("Mike", "Trout", "Male", 23, 1111, "Baseball")
    z = StudentAthlete("John", "Do", "Male", 33, 2222, "Soccer")

    print(x.getName())
    print(y.getName())
    print(z.getSport())
    print(StudentAthlete.instanceCount)


main()

"""
Output:

oggunderscore@oggunderscores-MacBook-Pro Exam2 % python3 main.py
Jose Cruz
Mike Trout | ID: 1111
Soccer
2

"""
