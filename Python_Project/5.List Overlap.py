#!/usr/bin/python3

import random

def AutoGenListOne():
    l1 = []
    count1 = 0
    while count1 < 10:
        new_element = random.randint(1, 50)
        l1.append(new_element)
        count1 += 1
    #print("l1 = ",l1)
    listone = tuple(l1)
    #print("l1 tuple:",listone)
    return listone

def AutoGenListTwo():
    l2 = []
    count2 = 0
    while count2 < 10:
        new_element = random.randint(1,50)
        l2.append(new_element)
        count2 += 1
    #print("l2 = ",l2)
    listtwo = tuple(l2)
    #print("l2 tuple:",listtwo)
    return listtwo

#a1 = [1,2,3,4,5,6,7,8,9,0]
#a2 = [1,2,3,4,5,11,12,13,14]
#l = []
#for i in a1:
#    if i in a2:
#        l.append(i)
#print(l)

def CompareList():
    l1st = AutoGenListOne()
    l2nd = AutoGenListTwo()
    print(" The first tuple is ", l1st,
          "\n",
          "The second tuple is",l2nd)
    l = []
    for i in l1st:
        #print(i)
        if i in l2nd:
            l.append(i)
    print("After comparison, the list composed of repeated list: ",l)
    return l

if __name__ == "__main__":
    CompareList()
