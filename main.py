import random

def  user_guess(x):
    random_number = random.randint(1,x)
    
    guess = 0
    while guess != random_number:
        guess = int (input(f'Guess the Computer number between 1 and {x} \n'))
        
        if guess < random_number:
            print('Try again, too low')
        elif guess > random_number:
            print('Try again, too high')
    
    print(f'Bingo!!! We have a winner, {random_number} is correct')
        
        
def pc_guess(x):
    low = 1
    high = x
    feedback = ''
    
    while feedback != 'c':
        guess = random.randint(low,high)
        random_number = int(input('Enter a random number'))
            
        