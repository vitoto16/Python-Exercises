"""
Write a function that takes an ordered list of numbers (a list where the elements are in
order from smallest to largest) and another number. The function decides whether or not
the given number is inside the list and returns (then prints) an appropriate boolean.

Extras:

Use binary search.
"""

def is_inside(num, some_list):
    return num in some_list

def is_inside_binary(num, some_list):
    left, right = 0, len(some_list) - 1
    while left <= right:
        middle = (left + right) // 2

        if num == some_list[middle]:
            return True

        if num > some_list[middle]:
            left = middle + 1
        elif num < some_list[middle]:
            right = middle - 1

a = [1, 3, 5, 30, 42, 43, 500]

print(is_inside_binary(1, a))
print(is_inside_binary(2, a))
print(is_inside_binary(3, a))
print(is_inside_binary(4, a))
print(is_inside_binary(5, a))

