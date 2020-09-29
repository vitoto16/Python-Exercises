"""
Write a program that asks the user how many Fibonnaci numbers to generate and then
generates them. Take this opportunity to think about how you can use functions. Make sure
to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the
sequence is the sum of the previous two numbers in the sequence. The sequence looks like
this: 1, 1, 2, 3, 5, 8, 13, …)
"""

def fibonacci_generator(times):
    a, b = 0, 1

    for i in range(0, times):
        yield f"{i+1}: {a}"
        a, b = b, a + b

times = int(input("How many numbers in the Fibonnaci sequence would you like to generate? "))

for i in fibonacci_generator(times):
    print(i)
