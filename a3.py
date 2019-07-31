# -*- coding: utf-8 -*-

# make a input() and judgment practise

print('Enter your birth please.')
day = eval(input('Day:'))
month = eval(input("Month:"))
year = eval(input("Year:"))
if month > 12:
    print('Wrong month entered.')
else:
    if year < 2001:
        print('You are a adult.')
    else:
        print('You are a juveniles.')

print("Your birthday is ",month,'.',day,'.',year,"(m/d/y).",sep='')