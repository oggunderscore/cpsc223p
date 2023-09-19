# Kevin Nguyen
# Exam 1 - 09/18/23 - 223P


def list_of_names(grades):
    names = []
    if len(grades) == 0:  # Assert that grade table exists
        return None
    for student_id, info in grades.items():  # Iterate over student_id as key object
        full_name = [
            info["firstname"],
            info["lastname"],
        ]  # Make full_name object [firstname, lastname]
        names.append(full_name)  # Append to list to print
    sorted_names = sorted(names, key=lambda x: x[1])  # Sort
    return sorted_names  # Return


def student_hw_avg(grades, id=None):  # Default value to none if not provided
    if len(grades) == 0:  # Assert that grade table exists
        print("Gradaebook is empty")
        return None
    if id in grades:  # Average hw scores by student id value
        scores = grades[id]["HW_scores"]  # Get List of only scores
        avg_score = sum(scores) / len(scores)  # Math
        return avg_score  # Return
    else:
        print("Student not found")  # Invalid ID Case
        return None


def class_hw_avg(grades, hw_index=0):  # Default index to 0 if not defined
    if len(grades) == 0:  # Assert that grade table exists
        print("Gradaebook is empty")
        return None
    total_score = 0
    num_students = len(grades)  # Baseline Length
    for student_id, info in grades.items():  # Iterate over student_id object as key
        if (
            len(info["HW_scores"]) > hw_index
        ):  # Asserting chosen hw_index is within boundaries
            total_score += info["HW_scores"][
                hw_index
            ]  # Add to total score prior to averaging
        else:
            print("HW Index out of range, returning None")  # Index out of range case
            return None
    if num_students > 0:  # Assert that human beings exist
        avg_score = total_score / num_students  # Math
        return avg_score  # Return
    else:
        return "No students found"  # No humans found case
