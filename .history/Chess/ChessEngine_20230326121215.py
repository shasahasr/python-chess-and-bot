"""
stores all the info abt the curret state of a chess game,
determines valid moves at the current state,
keep a move log,
"""


class GameState():
    def __init__(self):
        # board is 8x8, 2D list, each element has 2 characters
        # first char is color of piece (b or w) and second is the type of piece ('K', 'Q', 'R', 'B', 'N' or 'P')
        # "--" is an empty space
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.whiteToMove = True
        self.moveLog = []

class Move():
    def __init__(self, startSq, )