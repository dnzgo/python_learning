def add_student(student_list, name):
    student_list.append(name)

def show_students(student_list, score_list):
    for student, score in zip(student_list, score_list): # zip is a function that combines multiple lists together item-by-item.
        print(student + ' - ' + str(score))
