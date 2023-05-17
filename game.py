 #A number-guessing game

# Put your code here
from random import randint


b = randint(1, 100)

def algo(): 
    print('Try to guess my number!')
    count = 0
    while True:
        count += 1
        x = input()
        x != b
        if x[0] == '-':
            print('must be between 1 and 100')
        elif x.isdigit() == False:
            print('must be an integer')
        elif int(x) < b and int(x)>= 1:
            print('Your guess is too low')
        elif int(x) > b and int(x) <= 100:
            print('Your guess is too high')
        elif int(x) < 1:
            print ('must be between 1 and 100')
        elif int(x) > 100:
            print('must be between 1 and 100')
        else:
            return f'You are correct! Great job! with {count} tries'
            break
     


print(algo())


