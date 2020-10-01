"""
Given two .txt files that have lists of numbers in them, find the numbers that are
overlapping. One .txt file has a list of all prime numbers under 1000, and the other .txt
file has a list of happy numbers up to 1000.

(If you forgot, prime numbers are numbers that can’t be divided by any other number. And
yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia.)
"""

with open('primenumbers.txt', 'r') as f:
    file_content = f.read()

prime_numbers = file_content.split('\n')

with open('happynumbers.txt', 'r') as f:
    file_content = f.read()

happy_numbers = file_content.split('\n')

print(set(prime_numbers).intersection(set(happy_numbers)))
