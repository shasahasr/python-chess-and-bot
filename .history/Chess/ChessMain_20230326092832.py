"""
This is the main driver file,
Handles user input and displays current GameState object,
"""

import pygame as p
from Chess import ChessEngine

WIDTH = HEIGHT = 400  # 512 is also an option but quality of pieces isnt as good
DIMENSION = 8  # 8x8 chess board
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 # for animations
IMAGES = {}

'''
Initialize a global dictionary of images, only called ONCE in the main
'''
def loadImages():
    pieces = ['wp', 'WR', 'WN', 'wB', 'wK', 'we', 'bp', 'br', 'bN', 'be', 'bk', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
    # can acces an image by saying IMAGES['wp'] for example
            
'''
main driver for code
'''
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color('white'))
    gs = ChessEngine.GameState()
    loadImages() # only done once
    running = True 
    while running:
        for e in p.event.get():
            if e.type == p.QUIT():
                running = False
        
        clock.tick()
        
        

if __name__ == "__main__":
    main()