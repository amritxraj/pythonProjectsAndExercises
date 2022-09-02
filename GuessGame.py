import random
def guess(x):
    rand_num = random.randint(1,x)
    guess = 0
    while guess != rand_num:
        guess = int(input(f'Guess a number between 1 and {x}:'))
        if guess > rand_num:
            print('Oops, your guess too high')
        elif guess < rand_num:
            print('wooups, your guess too low')

    print(f'yo congrats budd, you guess number {rand_num} correctly')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!')

computer_guess(10)