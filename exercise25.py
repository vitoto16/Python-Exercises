import random
import time

game_on = True
left = 0
right = 100
guesses = 0
ANSWERS = ('too high', 'too low', 'correct')
MESSAGES = {
    'correct': (
        "Alright! I'm awesome!",
        "Piece of cake! :P",
        "I knew I could do it!"
        ),
    'too high': (
        "Okay, let's try something lower.",
        "Alright, gonna slow down now.",
        "What? Okay... I'm gonna get it right next time."
        ),
    'too low': (
        "Okay, now I'm going high!",
        "I think you are fooling me...",
        "Hmmmm okay, one more try."
        ),
    'known': (
        "Are you sure that's not your number? -> ",
        "I know that is your number... just tell me I'm right. -> ",
        "Stop playing, it's pretty obvious right now! -> "
        )
}

def is_valid(user_answer):
    return user_answer in ANSWERS

def take_guess():
    guess = random.randint(left, right)
    return guess

def force_correct():
    user_answer = input("Wait, I'm pretty sure that IS your number. ").lower()
    while user_answer != 'correct':
        user_answer = input(random.choice(MESSAGES['known'])).lower()
    return user_answer

welcome = '''Hi! Welcome to the reverse guessing game!

This is how the game works:

    Your job is to think of a number between 0 and 100.

    Mine is to guess what number is that!

For each guess I make, you need to give me a hint, whether my guess was:

"too high"

"too low"

"correct"

Okay, all set!
Lets begin!

(Press the "Enter" button to begin)'''

for sentence in welcome.split('\n'):
    print(sentence)
    if sentence:
        time.sleep(2)

input()
print("Okay, I'm ready to make my guess...")
time.sleep(3)

while game_on:
    print()
    if left <= right:
        guess = take_guess()
        guesses += 1
        time.sleep(1)
        print(f"My guess is... {guess}!! ")
        time.sleep(2)
        user_answer = input("So, how close was I?? -> ").lower()
        while not is_valid(user_answer):
            print("I'm sorry, but that does not tell me anything...")
            time.sleep(1)
            print()
            user_answer = input("Try choosing between 'too high', 'too low' and 'correct' -> ").lower()
    else:
        user_answer = force_correct()

    time.sleep(1)
    if user_answer == 'too high':
        print(random.choice(MESSAGES['too high']))
        right = guess - 1
    elif user_answer == 'too low':
        print(random.choice(MESSAGES['too low']))
        left = guess + 1
    else:
        print(random.choice(MESSAGES['correct']))
        time.sleep(1)
        print(f"And it only took me {guesses} guesses!")
        time.sleep(1)
        print("Thanks for playing!")
        game_on = False
