import random

print('Welcome to the number game\n')
print('Enter the range:\n')

lower = int(input('Enter the lower number:'))
upper = int(input('Enter the upper number:'))

number = random.randint(lower,upper)
no_chances = (upper-lower)//3 + 1

print(f'To win the game guess the number in {no_chances}')

def validate_guessed_number(guessed_number,number):
    if guessed_number == number:
        print('Congratulations!!\nYou won the game')
        exit(0)
    if guessed_number > number:
        print('Number you guessed is higher')
    else:
        print('Number guessed is smaller')

while no_chances:
    guessed_number = int(input('Guess the number:'))
    validate_guessed_number(guessed_number,number)
    no_chances -= 1
    if not no_chances:
        print('\nNo Chances left\n')
        print('Better luck next time!')
