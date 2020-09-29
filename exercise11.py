"""
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to
practice using functions, described below.
"""

def is_prime(num):
    if num == 1:
        return False
    else:
        for check in range(2, num):
            if num % check == 0:
                return False

    return True

num = int(input("Please, type in any number you wish -> "))

if is_prime(num):
    print("This number is prime!")
else:
    print("This number is not prime!")
