def get_weighted_average(students):
    homework = sum([i*0.1 for i in student['homework']])/len(student['homework'])
    quizzes = sum([i*0.3 for i in student['quizzes']])/len(student['quizzes'])
    tests = sum([i*0.6 for i in student['tests']])/len(student['tests'])
    weighted_average = homework +  quizzes + tests

    return round(weighted_average,2)