"""
stores all the info abt the curret state of a chess game,
determines valid moves at the current state,
keep a move log,
"""


class GameState():
    def __init__(self):
        self.board = [
            ["bR", "bN"
             ", "bB"
             ", "bQ", "bK"
             "bB", "bN", "bR"],
            ["bp", , "bp", "bp"., "bp"
             "bp",
             "bp",
             "bo", "bp"],
        ]
