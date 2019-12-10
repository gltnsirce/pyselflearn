#!/usr/bin/python3
print('This is a self-study programming.')
print('Project Name: Odd or Even')
print('###############################################################')

print('Enter according to the following criteria:')

Num = int(input('1. Enter the first number:'))
check = int(input("2. Give me a number to divide by: "))

def judge():
    if Num % 4 == 0:
        print(Num, "is a multiple of 4.")
    elif Num % 2 == 0:
        print(Num, "is a even number.")
    else:
        print(Num, "is an odd number.")

def divides():
    if Num % check == 0:
        print(Num,"divides evenly by", check)
    else:
        print(Num, "dose not divide evenly by", check)

if __name__ == "__main__":
    judge()
    divides()
