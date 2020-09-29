"""
Write a program (function!) that takes a list and returns a new list that contains all
the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and
another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different
function.
"""

def remove_dups_loop(some_list):
    new_list = list()
    for item in some_list:
        if item not in new_list:
            new_list.append(item)
    return new_list

def remove_dups_set(some_list):
    return set(some_list)

some_list = [1, 1, 2, 3, 5, 5, 5, 8, 13, 13, 21, 36, 21, 13, 3]

print(remove_dups_loop(some_list))
print(remove_dups_set(some_list))
