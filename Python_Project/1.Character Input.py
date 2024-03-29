#!/usr/bin/python3

import time;

print("Program description:")
print("Create a program that asks the user to enter their name and their age.",
      "\n",
      "Print out a message addressed to them that tells them the year that they will turn 100 years old.")
print('##############################################################')

name = input('Enter your name:')
age = int(input('Please enter your age:'))
print(name,"is",age,"years old.")

current_year = time.strftime('%Y',time.localtime())
right_year = int(current_year)
target_year = (right_year - age) + 100

print(name,'will be 100 years old in',target_year)
