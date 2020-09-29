"""
Write a program (using functions!) that asks the user for a long string containing multiple
words. Print back to the user the same string, except with the words in backwards order.
For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
shown back to me.
"""

def reverse_words(some_string):
    splitted_string = some_string.split(' ')
    separator = ' '

    return separator.join(splitted_string[::-1])

user_string = input("Please, type in any sentence you wish -> ")

print(reverse_words(user_string))
