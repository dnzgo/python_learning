import math_tools
import student_tools

students = ['deniz', 'emir']
scores = [70, 80]

student = input('students name: ')
student_tools.add_student(students, student)
score = float(input("student's score: "))
scores.append(score)

student_tools.show_students(student_list = students, score_list = scores)
avg = math_tools.calculate_average(scores)
min_score = math_tools.find_lowest(scores)
max_score = math_tools.find_highest(scores)
print('average score: ' + str(avg) + '\nmin score: ' + str(min_score) + '\nmax_score: ' + str(max_score))


