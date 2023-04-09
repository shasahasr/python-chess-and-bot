"""
This is the main driver file,
Handles user input and displays current GameState object,
"""

import pygame as p
from Chess import ChessEngine

WIDTH = HEIGHT = 400  # 512 is also an option but quality of pieces isnt as good
DIMENSION = 8  # 8x8 chess board
SQ_SIZE = HEIGHT // DIMENSION
