# -*- coding = utf-8 -*-

h = eval(input('Input your height(Meter):'))
w = eval(input('Input your weight(KG):'))

x = w/h/h

if x < 18.5:
    print('You are too skinny.')
elif x > 18.5 and x < 25:
    print('You are health.')
elif x > 25 and x < 28:
    print('Your weight has a litte overwight.')
else:
    print('You are too fat~!')

print('Your BMI is',x)
