"""
"=====Roll_a_dice====="
"""
print('==========ROLL A DICE==========')
print("This is a game based on the 'Roll a dice'")
print('Enter 0 to exit.')
from random import randint
Dice = randint(1,6)
user = 0
computer = 0
t = 1
Number = int(input('Choose a number from 1 to 6: '))
while t != 0:
    if Number == 0:
        print('The end')
        print('Developed by:_WyThdev_...')
        t = 0
    else:
        if Number == Dice:
            user = user+1
            print('          =====You win!=====')
            print('          ___Scoreboard:___ \n     --You: {} \n    --Computer: {}'.format(user, computer))
            print('        Total of tentatives: {}'.format(computer + user))
            print('=====ROLL A DICE=====')
            Dice = randint(1,6)
            Number = int(input('Choose a number from 1 to 6: ')) 
        elif (Number != Dice) and (Number >= 1) and (Number <= 6):
            computer = computer+1
            print('          -----You lose!-----')
            print('Your number: {} \nComputer number: {}'.format(Number, Dice))
            print('          ___Scoreboard:___ \n     --You: {} \n    --Computer: {}'.format(user, computer))
            print('        Total of tentatives: {}'.format(computer + user))
            print('=====ROLL A DICE=====')
            Dice = randint(1,6)
            Number = int(input('Choose a number from 1 to 6: '))
        else:
            print('ERROR!!! TRY AGAIN')
            print('=====ROLL A DICE=====')
            Dice = randint(1,6)
            Number = int(input('Choose a number from 1 to 6: '))
