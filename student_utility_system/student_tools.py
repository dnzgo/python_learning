def add_student(student_list, name):
    """
    this function helps to add new students name to student_list
    """
    student_list.append(name)


def show_students(student_list, score_list):
    """
    this function prints all students with their score
    """
    for student, score in zip(student_list, score_list): # zip is a function that combines multiple lists together item-by-item.
        print(student + ' - ' + str(score))
