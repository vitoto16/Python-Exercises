"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
"""

from datetime import datetime

name = input("Please, type your name and hit Enter -> ")
age = int(input("Please, type your age and hit Enter -> "))
num = int(input("Please, type any number you wish -> "))


year_100 = int(datetime.now().strftime('%Y')) + 100 - age

print(f"{name}, you are going to turn 100yo in {year_100}\n" * num)
