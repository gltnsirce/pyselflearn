#!/usr/bin/python3

print('Create a program that asks the user for a number and then prints out a list of all the divisors of that number.')
print('If you don’t know what a divisor is, it is a number that divides evenly into another number.',
      "\n",
      'For example, 13 is a divisor of 26 because 26 / 13 has no remainder.')

userNumber = int(input('Enter a number casually:'))

count = userNumber

while count > 1:
    count -= 1
    if userNumber % count == 0:
        print('The number ',"'" , userNumber , "'",' can be divisible by ', count , '.',sep="")
