import math_tools # importing module
from student_tools import add_student, show_students as print_s # importing specific functions from module, giving an alias to a function
# from module import * --> means copy all functions of that module to this file, we can call functions without dot notation
students = ['deniz', 'emir']
scores = [70, 80]

student = input('students name: ')
add_student(students, student)
score = float(input("student's score: "))
scores.append(score)

print_s(student_list = students, score_list = scores)
avg = math_tools.calculate_average(scores)
min_score = math_tools.find_lowest(scores)
max_score = math_tools.find_highest(scores)
print('average score: ' + str(avg) + '\nmin score: ' + str(min_score) + '\nmax_score: ' + str(max_score))

