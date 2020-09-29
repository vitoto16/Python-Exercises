"""
Write a password generator in Python. Be creative with how you generate passwords - strong
passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
The passwords should be random, generating a new password every time the user asks for a
new password. Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or
two from a list.
"""

from pyemojify import emojify
import string
import random

LOWERS = tuple(string.ascii_lowercase)
UPPERS = tuple(string.ascii_uppercase)
DIGITS = tuple(string.digits)
SYMBOLS = tuple(string.punctuation)

def is_valid(user_input):
    values = ('weak', 'average', 'strong')
    return (user_input in values)

def password_generator(difficulty):
    if difficulty == 'weak':
        for i in range(8):
            yield random.choice(LOWERS)
    elif difficulty == 'average':
        choices = (LOWERS, UPPERS, DIGITS)
        for i in range(1, random.randint(8, 16)):
            charset = random.choice(choices)
            yield random.choice(charset)
    elif difficulty == 'strong':
        choices = (LOWERS, UPPERS, DIGITS, SYMBOLS)
        for i in range(1, random.randint(12, 16)):
            charset = random.choice(choices)
            yield random.choice(charset)

print('''This is a password generator! Available strenght choices are:

STRONG
AVERAGE
WEAK
''')
user_input = input("Please, type in how strong you want your password to be: ").lower()
while not is_valid(user_input):
    print(f"'{user_input}' is not a valid strenght value.")
    user_input = input("Please, type in a valid strenght value for your password: ").lower()

new_password = ''.join([x for x in password_generator(user_input)])

message = emojify(f"Your new {user_input} password is: {new_password} :smile: :smile: :smile:" )

print(message)
