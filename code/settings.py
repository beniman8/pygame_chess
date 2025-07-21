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
    'light_green':(234,235,200),
    'dark_green':(119,154,88),
    'light_trace':(244,247,116),
    'dark_trace':(172,195,51),
    'light_brown':(235,209,166),
    'dark_brown':(165,117,80),
    'light_blue':(229,228,200),
    'dark_blue':(60,95,135),   
    'light_gray':(120,119,118),
    'dark_gray':(86,85,84),
    
    
    
}