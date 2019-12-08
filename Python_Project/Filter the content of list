#!/usr/bin/python3

import random

print('Program description:',"\n",'Filter the content of list.')

userNumber = int(input('Please enter a arbitrary number:'))

def AutoGenList():
    l = []
    count = 0
    while count < 10:
        new_element = random.randint(0,100)
        l.append(new_element)
        count += 1
    #print("Radom list:",l)
    new_List = sorted(l)
    #print("New List:",new_List)
    return new_List

def AddNewElement():
    tempList = AutoGenList()
    tempList.append(userNumber)
    tempList = sorted(tempList)
    return  tempList

def printElement():
    freshList = AddNewElement()
    for element in freshList:
        print(element)

if __name__ == "__main__":
    printElement()
