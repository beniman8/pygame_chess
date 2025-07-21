import pygame
import os 

from sound import Sound
from theme import Theme
from settings import COLORS

class Config:
    
    def __init__(self):
        self.themes = []
        self._add_themes()
        self.idx = 0
        self.theme = self.themes[self.idx]
        
        #font
        self.font = pygame.font.SysFont('monospace',18,bold=True)
        self.move_sound = Sound(os.path.join('audio/move.wav'))
        self.capture_sound = Sound(os.path.join('audio/capture.wav'))
    
    def change_theme(self):
        self.idx +=1
        self.idx %= len(self.themes)
        self.theme = self.themes[self.idx]
    
    def _add_themes(self):
        green = Theme(COLORS['light_green'],COLORS['dark_green'],COLORS['light_trace'],COLORS['dark_trace'],'#C86464','#C84646')
        brown = Theme(COLORS['light_brown'],COLORS['dark_brown'],(245,234,100),(209,185,59),'#C86464','#C84646')
        blue = Theme(COLORS['light_blue'],COLORS['dark_blue'],(123,187,227),(43,119,191),'#C86464','#C84646')
        gray = Theme(COLORS['light_gray'],COLORS['dark_gray'],(99,126,143),(82,102,128),'#C86464','#C84646')
    
        self.themes = [green,brown,blue,gray]
    
