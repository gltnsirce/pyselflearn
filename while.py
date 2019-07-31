'''
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
    print(n,sum)
print(sum)
'''
#######################################

'''
sum = 1
n = 0
while n < 10001:
    n = n + 1
    sum = sum + n
    if n == 666:
        break
    print(n,sum)
print(sum)
'''

########################################
'''
l = ['Bart','Lisa','Adam']

#x = len(l)

for name in l:
    print('Hello',name,end='...\n')
    if name == "Lisa":
        break

#print(x,l)
'''

########################################

'''
n = 0
while n < 10:
    continue
    n = n + 1
    print("test",end="\n")
'''