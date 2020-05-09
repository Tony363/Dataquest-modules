# Intro to Programming Using Python - Assignment #3
# Completed by:

# Be sure to read the instructions carefully!

# 1. Create three dictionaries, each one will contain information about a particular student: Steve, Alice and Tyler
#   a. Assign each dictionary to a variable – eg. steve, alice and tyler
#   b. Create the following keys: name, homework, quizzes, and tests
#   c. Set the value of the name key to the name of the student – e.g. Steve's name should be "Steve"
#   d. Set the other keys – e.g. homework, quizzes, and tests – to empty lists (we'll fill them in later)
#   e. Print these empty dictionaries

# 2. Now fill in the dictionaries above with the following scores and print the dictionaries:
# Steve
#   Homework: 90, 97, 75, 92
#   Quizzes: 88, 40, 94
#   Tests: 75, 90
# Alice
#   Homework: 100, 92, 98, 100
#   Quizzes: 82, 83, 91
#   Tests: 89, 97
# Tyler
#   Homework: 0, 87, 75, 22
#   Quizzes: 0, 75, 78
#   Tests: 100, 100



# 3. Create a list called students that contains your three students and print the list



# 4. Loop over your students list and print out the following for each student:
#   - Name: (print out the student's name)
#   - Homework: (print out the student's homework)
#   - Quizzes: (print out the student's quizzes)
#   - Tests: (print out the student's tests )


# 5. Define a function to calculate the average of a list
#   a. Define a function called average() that has one argument, a list of numbers
#   b. Inside the function, use the built-in Python functions sum() and len() to calculate the average
#   c. Return the result 
#   d. Test it out to make sure it works


# 6. Write a function to calculate the weighted average score for a student
#   a. Define a function called get_weighted_average() that takes one argument: student (see the dictionaries we created above)
#   b. Use your average() function to calculate the average of the student's homework, quizzes, and test scores
#   d. Return the weighted average score for each student (homework is 10%, quizzes are 30%, and tests are 60%  of the grade).
#   e. Test out your get_weighted_average() function on each student


# 7. Write a function to convert a grade into a letter grade
#   a. Define a function called get_letter_grade() that has one argument called score (a number)
#   b. Inside your function, use if / elif /else to return the following letter grades:
#       - 90 or above: “A"
#       - 80 or above: “B"
#       - 70 or above: “C"
#       - 60 or above: “D"
#       - Below 60: “F"
#   c. Test it out on a few different numbers to make sure it works properly
#   d. Use a for loop to get each student's letter grade


# 8. Write a function to calculate the class average
#   a. Create a function called get_class_average() that has one argument, students (a list of dictionaries)
#   b. Inside the function, create a temporary empty list called results to store each student's grade
#   c. Loop over the list of students, appending each student's grade into your results list
#   d. Finally, return the average of the results
#   e. Test out your function by printing out the class average


# 9. The class has now a new student, Thomas, with the following grades:
#   Homework: 90, 85, 80, 0
#   Quizzes: 80, 100, 87
#   Tests: 85, 90
#   a. Create a dictionary for Thomas (as you did in #1)
#   b. add him to the class, by appending the dictionary to your list of students
#   c. Calculate the new class average and print your results

# BONUS: Move all of the functions out of this file and into another Python file
# called grading_functions.py. Then import them into this file so that it runs.

from sklearn.datasets import fetch_openml
from grading_function import get_weighted_average, class_average

steve = {"name":"Steve",
        "homework":[],
        "quizzes": [],
        "tests":[]}
alice = {"name":"Alice",
        "homework":[],
        "quizzes":[],
        "tests":[]}
tyler = {"name":"Tyler",
        "homework":[],
        "quizzes":[],
        "tests":[]}
print(steve)
print(alice)
print(tyler)

steve['homework'] = [90,97,75,92]
steve['quizzes'] = [88,40,94]
steve['tests'] = [75,90]

alice['homework'] = [100,92,98,100]
alice['quizzes'] = [82,83,91]
alice['tests'] = [89,97]

tyler['homework'] = [0,87,75,22]
tyler['quizzes'] = [0,75,78]
tyler['tests'] = [100,100]

Thomas = {'name':'Thomas',
    'homework':[],
    'quizzes':[],
    'Tests':[],
}
Thomas['homework'] = [90,85,80,0]
Thomas['quizzes'] = [80,100,87]
Thomas['tests'] = [85,90]

students = [steve, alice, tyler]
students.append(Thomas)

print(students)

for student in students:
    print("Name:", student['name'])
    print("Homework:", student['homework'])
    print("Quizzes:", student['quizzes'])
    print("Tests:", student['tests'])

lst = steve['homework']
sum(lst)
len(lst)
avg_steve_homework = float(sum(lst))/len(lst)
print("Homework Average Score:")
print(avg_steve_homework)

lst1 = steve['quizzes']
sum(lst1)
len(lst1)
avg_steve_quizzes = float(sum(lst1))/len(lst1)
print("Quizzes average score:")
print(avg_steve_quizzes)

lst2 = steve['tests']
sum(lst2)
len(lst2)
avg_steve_tests = float(sum(lst2))/len(lst2)
print("Tests average score:")
print(avg_steve_tests)


print('alice\'s weighted average is {}'.format(get_weighted_average(students,1)))
print('steve\'s weighted average is {}'.format(get_weighted_average(students, 0)))
print('tyler\'s weighted average is {}'.format(get_weighted_average(students,2)))

print(class_average(students))







