"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the
number, then tell them whether they guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""

import random

game_on = True
guesses = 0
num = random.randint(1, 9)

def compare(guess, num):
    if guess > num:
        print(f"You guessed too high!")
        return False
    elif guess < num:
        print(f"You guessed too low!")
        return False
    else:
        print(f"You got it! The number was {num}!")
        return True

def play_again():
    if input("Type 'exit' if you do not want to play again: ").lower() == 'exit':
        return False
    else:
        return True

print('''This is a guessing game! A random number from 1 - 9 is going to be generated.
Your job is to find out which number that is!''')

while game_on:
    guess = input("What number do you think has been generated?")
    while not guess.isdigit():
        print(f"{guess} is not a valid number.")
        guess = input("Please type in your guess: ")

    guesses += 1

    if compare(int(guess), num):
        print(f"You have made {guesses} guesses!")
        if play_again():
            num = random.randint(1, 9)
            guesses = 0
        else:
            game_on = False
