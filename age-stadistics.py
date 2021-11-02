## Proyecto Ejercicio - 3

import random

opc = int()
list_ages = []

def menu():
    print('''
Menu:
1. Store in a list the ages of the students
2. Obtain the oldest and youngest age
3. Calculate the average
4. Modify an age
5. Eliminate an age
6. Calculate and display the median
''')

    while True:
        try:
            global opc
            opc = int(input('Select an option: '))
        except:
            print('Invalid command, please try again.')
            continue
        break
menu()

n = int()
if (opc == 1):
    while True:
        try:
            n = int(input('Indicate the number of ages to be stored: '))
        except ValueError:
            print('Error, please enter an integer')
            continue
        break
    for i in range(n):
        list_ages.append(random.randint(6, 14))
    print(list_ages)
    menu()

if (opc == 2):
    max = max(list_ages)
    min = min(list_ages)
    print('The oldest is', max)
    print('The youngest is', min)
    menu()

if (opc == 3):
    average = sum(list_ages) / n
    print('The average age is:', average)
    menu()

if (opc == 4):
    ind = int(input('Indicate the index of the age you want to change: ')) - 1
    list_ages[ind] = int(input('Enter the new value: '))
    print(list_ages)
    menu()

if (opc == 5):
    ind = int(input('Indicate the index of the age you want to eliminate: ')) - 1
    del list_ages[ind]
    print('Eliminated. Remaining ages stored:', list_ages)
    menu()

if (opc == 6):
    list_ages.sort()
    middle_index = n//2
    if (n % 2 == 0):
        list1 = list_ages[:middle_index]
        list2 = list_ages[middle_index:]
        median = list1[-1] + list2[0] / 2
        print('The median is:', median)
    else:
        print('The median is: ' + str(list_ages[middle_index]))

if (opc > 6):
    print('The option entered is not in the menu.')