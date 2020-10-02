"""
This exercise is Part 2 of 4 of the Tic Tac Toe exercise series.

As you may have guessed, we are trying to build up to a full tic-tac-toe board. However,
this is significantly more than half an hour of coding, so we’re doing it in pieces.

Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe,
not worrying about how the moves were made.

If a game of Tic Tac Toe is represented as a list of lists, like so:

game = [[1, 2, 0],
    [2, 1, 0],
    [2, 1, 1]]
where a 0 means an empty square, a 1 means that player 1 put their token in that space,
and a 2 means that player 2 put their token in that space.

Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board,
tell me whether anyone has won, and tell me which player won, if any. A Tic Tac Toe win
is 3 in a row - either in a row, a column, or a diagonal. Don’t worry about the case where
TWO people have won - assume that in every board there will only be one winner.

Here are some more examples to work with:

winner_is_2 = [[2, 2, 0],
    [2, 1, 0],
    [2, 1, 1]]

winner_is_1 = [[1, 2, 0],
    [2, 1, 0],
    [2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
    [2, 1, 0],
    [2, 1, 1]]

no_winner = [[1, 2, 0],
    [2, 1, 0],
    [2, 1, 2]]

also_no_winner = [[1, 2, 0],
    [2, 1, 0],
    [2, 1, 0]]
"""

import numpy as np

def check_winner(board_matrix):
    index = 0
    while index < len(board_matrix):
        row = board_matrix[index, :]
        column = board_matrix[:, index]
        if np.prod(row) == 8 or np.prod(column) == 8:
            return 'player 2'
        elif np.prod(row) == 1 or np.prod(column) == 1:
            return 'player 1'
        index += 1

    diagonal1 = board_matrix.diagonal()
    diagonal2 = np.fliplr(board_matrix).diagonal()
    if np.prod(diagonal1) == 8 or np.prod(diagonal2) == 8:
        return 'player 2'
    elif np.prod(diagonal1) == 1 or np.prod(diagonal2) == 1:
        return 'player 1'

    return None

a = np.array([
        [1, 2, 0],
        [2, 1, 0],
        [2, 1, 0]
])

b = np.array([
        [1, 2, 0],
        [2, 1, 0],
        [2, 1, 1]
])

c = np.array([
        [2, 2, 0],
        [2, 1, 0],
        [2, 1, 1]
])

d = np.array([
        [1, 2, 2],
        [2, 2, 1],
        [2, 1, 1]
])

e = np.array([
        [1, 1, 1],
        [2, 1, 0],
        [2, 2, 2]
])

print(check_winner(a)) # Must print None
print(check_winner(b)) # Must print 'player 1'
print(check_winner(c)) # Must print 'player 2'
print(check_winner(d)) # Must print 'player 2'
print(check_winner(e)) # Must print 'player 1'
