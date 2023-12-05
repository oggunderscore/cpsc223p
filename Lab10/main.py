import csv
from collections import defaultdict

# Kevin Nguyen
# CPSC 223P


# Function to calculate average age per class
def calculate_average_age(data):
    class_ages = defaultdict(list)

    for student in data:
        class_ages[student["Class"]].append(int(student["Age"]))

    average_ages = {
        class_: sum(ages) / len(ages) for class_, ages in class_ages.items()
    }
    return average_ages


# Read the CSV file
with open("input.csv", "r") as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Calculate and print the total number of students
total_students = len(data)
print(f"Total number of students: {total_students}")

# Calculate and print the average age of students per class
average_ages = calculate_average_age(data)
for class_, age in average_ages.items():
    print(f"Average age of students in {class_} grade: {age:.2f} years")

# Create a new CSV file for 10th-grade students
tenth_grade_students = [student for student in data if student["Class"] == "10th"]
fieldnames = ["Name", "Roll No."]

with open("tenth_grade_students.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Write header
    writer.writeheader()

    # Write data
    for student in tenth_grade_students:
        writer.writerow({"Name": student["Name"], "Roll No.": student["Roll No."]})

print("CSV file for 10th grade students created successfully.")
