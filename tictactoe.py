"""
Tic Tac Toe Map
=================
 p7 | p8 | p9
----|----|----
 p4 | p5 | p6
----|----|----
 p1 | p2 | p3

Possible values for each position are "x", "o" or None.
'x' is always played by the first player
'o' is always played by the second player
None is empty space
"""

def play(board, turn):
    """
    Plays next moviment based on the received current state(board) of the game.
    This function must returns the integer related to the position.
    So, if you want to play on p3, you must return 3, and so on.
    You are only allowed to play on positions which are currently None.
    The turn parameter will be always between 1 and 9, and it is
    related to the current turn. So, if three positions are occupied,
    the received turn parameter will be 4.
    If this function returns an invalid value, then this player loses the match.

    Example of how this function will be called
    >>> play({'p1': 'x', 'p2': None, 'p3': None, 'p4': None, 'p5': 'o', 'p6': None, 'p7': None, 'p8': None, 'p9': 'x'}, 4)
    2
    """
    if board['p1'] is None:
        return 1
    elif board['p2'] is None:
        return 2
    elif board['p3'] is None:
        return 3
    elif board['p4'] is None:
        return 4
    elif board['p5'] is None:
        return 5
    elif board['p6'] is None:
        return 6
    elif board['p7'] is None:
        return 7
    elif board['p8'] is None:
        return 8
    elif board['p9'] is None:
        return 9

# Please, don't change the lines below
# You may change ony the play() function implementation
import sys
import ast

board = ast.literal_eval(sys.argv[1])
turn = int(sys.argv[2])

print(play(board, turn))
