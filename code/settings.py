'''
This area stores all my settings and constants that can be used throughout the game
'''

import pygame
import sys
from os.path import join
from os import walk  


#Screen dimensions
WINDOW_WIDTH,WINDOW_HEIGHT = 800,800

#Board dimensions 
BOARD_ROWS,BOARD_COLS =8,8
SQUARE_SIZE = WINDOW_WIDTH // BOARD_COLS


COLORS ={
    'black':'#000000',
    'beige':'#eaebc8',
    'green':'#779a58',
    
}