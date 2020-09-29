"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and
makes a new list of only the first and last elements of the given list. For practice,
write this code inside a function.
"""

def list_tips(some_list):
    return [some_list[0], some_list[-1]]

a = [5, 10, 15, 20, 25]

print(list_tips(a))
