import statistics

admin= {'john': '9', 'sam': 'pass69'}
studentDict = {'Jeff': [78,88,93],
               'Alex': [92,76,88],
               'Sam' : [89,92,93]}
def enterGrades():
    input_1= input(' Enter Student name: ')
    input_2= float(input('Enter Student grade: '))
    
    if input_1 in studentDict:
        print('adding grades...')
        # converting input from user into float before appending /
        studentDict[input_1].append(float(input_2))
        print(studentDict)
    else:
        print('Student is not part of the org!!')


def removeStudent():
    nametoRemove= input('Who would you like to remove: ')
    if nametoRemove in studentDict: 
        print('Removing student...')
        del studentDict[nametoRemove]
    print (studentDict)

def studentAverage_Grade():
    for eachStudent in studentDict:
        gradeList = studentDict[eachStudent]
        avgGrade = statistics.mean(gradeList)
        print(eachStudent, ' has an average of', avgGrade)


def logging():

    attempts= 0 

    while True: 
        login= input("Enter username: ")
        passW= input('Enter Password')
        if login in admin and admin[login]== passW:
                print('Logging in ')
                while True:
                    main()
        else:
            attempts+=1
            print(f'Incorrect , Please try again. Attempts: {attempts} ')
    

def main():
    print("""
            Welcome to Sabin's Application
          
            [1]- Enter Student Grades 
            [2]- Remove Student
            [3]- Student Average Grade
            [4]- Exit """)
    action= int(input('What would you like to do today: '))
    
    if action == 1:
        enterGrades()
    elif action == 2:
       removeStudent()
    elif action == 3:
        studentAverage_Grade()
    elif action == 4:
        exit()
    else:
        print('No valid choice was given, try again')

logging()