#!/usr/bin/python3

import random

print('I will auto generate a list with 20 elements if you do not want to enter a list and the members.')
print('=============================================================================================================')

def DealUserList():
    ul = []
    newList = []
    UserList = list(map(int, input("Enter the list's elements and split by" + "\033[0;31;40m\t','\033[0m" + ":").split(",")))
    for x in UserList:
        if x % 2 == 0:
            newList.append(x)
    return newList

def AutoGenList():
    l = []
    count = 0
    while count < 20:
        new_element = random.randint(1, 100)
        l.append(new_element)
        count += 1
    return l

def EvenList():
    legacyList = AutoGenList()
    print("\nThe auto-generated list is",legacyList)
    newList = []
    for x in legacyList:
        if x % 2 == 0:
            newList.append(x)
    return newList

if __name__ == '__main__':
    judge = input('\nEnter Y/y if you want to enter the list by yourself:')
    if judge == 'Y' or judge == 'y':
        print("In your list, the new list of even number is",DealUserList())
    else:
        print("\nIn the auto-generated list, the new list of even number is",EvenList())
