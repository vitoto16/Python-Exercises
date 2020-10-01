"""
This exercise is Part 1 of 4 of the Tic Tac Toe exercise series.
Time for some fake graphics! Let’s say we want to draw game boards that look like this:

 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for
chess, 19x19 for Go, and many more).

Ask the user what size game board they want to draw, and draw it for them to the screen
using Python’s print statement.

Remember that in Python 3, printing to the screen is accomplished by

  print("Thing to show on screen")
"""

def is_valid(user_size):
    return user_size.isdigit()

def draw_board(size):
    y_borders = " ---"
    x_borders = "|   "

    for i in range(size):
        print(y_borders * size)
        print(x_borders * (size + 1))
        if i == size-1:
            print(y_borders * size)

user_size = input("Please, type in the size of your board: ")
while not is_valid(user_size):
    print(f"{user_size} is not a valid size for the board")
    user_size = input("Please, type in a valid board size: ")

draw_board(int(user_size))
