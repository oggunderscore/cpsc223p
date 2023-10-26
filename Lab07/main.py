from people import Faculty, Student

faculty_list = []
student_list = []

while True:
    print("\n\t========= TUFFY TITAN STUDENT / FACULTY MAIN MENU =========\n")
    print("1. Add faculty")
    print("2. Print faculty")
    print("3. Add student")
    print("4. Print student")
    print("5. Exit\n")

    choice = input("Enter your choice: ")

    if choice == "1":
        first_name = input("Enter faculty's first name: ")
        last_name = input("Enter faculty's last name: ")
        department = input("Enter faculty's department: ")

        faculty = Faculty(first_name, last_name, department)
        faculty_list.append(faculty)
        print("Faculty added.")

    elif choice == "2":
        print("\n======================= FACULTY =======================")
        print(f"Record  {'Name':20}  {'Department':25}")
        print("======  ====================  =========================")
        for index, faculty in enumerate(faculty_list, start=1):
            print(
                f"{index:6}  {(faculty.firstname + ' ' + faculty.lastname):20}  {faculty.department:25}"
            )

    elif choice == "3":
        first_name = input("Enter student's first name: ")
        last_name = input("Enter student's last name: ")
        class_year = input("Enter student's class year: ")
        major = input("Enter student's major: ")

        print("Choose a faculty advisor from the list:")
        for index, faculty in enumerate(faculty_list, start=1):
            print(
                f"{index:6}  {(faculty.firstname + ' ' + faculty.lastname):20}  {faculty.department:25}"
            )

        advisor_index = (
            int(input("Enter the record number of the faculty advisor: ")) - 1
        )

        if 0 <= advisor_index < len(faculty_list):
            student = Student(first_name, last_name)
            student.set_class(class_year)
            student.set_major(major)
            student.set_advisor(faculty_list[advisor_index])
            student_list.append(student)
            print("Student added.")
        else:
            print("Invalid faculty advisor selection. Student not added.")

    elif choice == "4":
        print(
            "\n===================================== STUDENTS ======================================"
        )
        print(f"{'Name':20}  {'Class':9}  {'Major':25}  {'Advisor':20}")
        print(
            "====================  =========  =========================  ========================="
        )
        for student in student_list:
            print(
                f"{(student.firstname + ' ' + student.lastname):20}  {student.classyear:9}  {student.major:25}  {(student.advisor.firstname + ' ' + student.advisor.lastname):20}"
            )

    elif choice == "5":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please choose a valid option (1-5).")
