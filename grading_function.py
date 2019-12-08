def get_weighted_average(students,n):
    homework = sum([i*0.1 for i in students[n]['homework']])/len(students[n]['homework'])
    quizzes = sum([i*0.3 for i in students[n]['quizzes']])/len(students[n]['quizzes'])
    tests = sum([i*0.6 for i in students[n]['tests']])/len(students[n]['tests'])
    weighted_average = homework +  quizzes + tests

    return round(weighted_average,2)