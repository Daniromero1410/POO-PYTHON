import random

def guess(x):
    random_number = random.randint(1,x)
    guess= 0
    while guess != random_number:
        guess= int(input(f"guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again, too low ")

        elif guess > random_number:
            print("Sorry, guess again, too high")


    print("Congrats you guessed the number")
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low  #Could also be high b/c low = high
        feedback = input(f"Is {guess}, too high, too low, or correct (C)??").lower()
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low == guess + 1



    print(f'the computer guessed your number,{guess},correctly!')



computer_guess(10)
