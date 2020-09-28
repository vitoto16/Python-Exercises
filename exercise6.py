"""
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
"""

user_input = input("Please type in any word you wish -> ")

if user_input == user_input[::-1]:
    print(f"{user_input} is a palindrome!")
else:
    print(f"{user_input} is not a palindrome!")
