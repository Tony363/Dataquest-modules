def get_weighted_average(students,n):
    # List = []
    # for i in students[n]['homework']:
    #     scores = i*0.1
    #     List.append(scores)
    # adding = sum(List)
    # length = len(students[n]['homework'])
    # average_homework = adding/length


    homework = sum([i*0.1 for i in students[n]['homework']])/len(students[n]['homework'])
    quizzes = sum([i*0.3 for i in students[n]['quizzes']])/len(students[n]['quizzes'])
    tests = sum([i*0.6 for i in students[n]['tests']])/len(students[n]['tests'])
    weighted_average = homework +  quizzes + tests

    return round(weighted_average,2)

def class_average(students):
    Number_class = len(students)
    List = []
    
    for i in range(Number_class):
        List.append(get_weighted_average(students,i))
    add = sum(List)
    return add/Number_class

    

    