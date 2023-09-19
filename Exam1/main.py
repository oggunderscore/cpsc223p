from test import list_of_names, student_hw_avg, class_hw_avg

# grades dictionary
grades = {
    343: {"firstname": "John", "lastname": "Stockton", "HW_scores": [87, 69, 96, 90]},
    12: {
        "firstname": "Martina",
        "lastname": "Navratilova",
        "HW_scores": [78, 89, 86, 92],
    },
    500: {"firstname": "Julio", "lastname": "Chavez", "HW_scores": [88, 89, 100, 100]},
    211: {"firstname": "Mary", "lastname": "Pham", "HW_scores": [80, 99, 77, 100]},
}

print(list_of_names(grades))
print(student_hw_avg(grades, id=12))
print(class_hw_avg(grades, hw_index=0))

print("Empty Case\n")
empty = {}

print(list_of_names(empty))
print(student_hw_avg(empty, id=12))
print(class_hw_avg(empty, hw_index=0))

print("Other Case\n")

print(list_of_names(grades))
print(student_hw_avg(grades, id=1))
print(class_hw_avg(grades, hw_index=5))
