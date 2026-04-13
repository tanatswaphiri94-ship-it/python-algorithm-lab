#dictioanry showing where to store data
students={}
number_of_students = int(input('number: '))
# showing the number of stuents
for i in range (number_of_students):
    total = 0
    student_name = input ('name:or done to stop ')

    score = int(input('score: '))
    students ={student_name : score}
    print(students)
# calculation of average 
average = total/number_of_students
print (average)

#level 2

while True :
    score = float(input('enter score'))
    if score >= 0 and score <=100:
        print('correct')
        break
    else:
        print('invalid score')

#level 3

import random 
number=random.number(1,100)
attempts = 0

while True:
    guessed = int (input('guess the number'))
    attempts += 1
    if guessed < number:
        print ('too low')
    elif guessed > number :
        print ("too high")
    else:
        print (f'done{number}in{attempts}')
        break       
    



      

