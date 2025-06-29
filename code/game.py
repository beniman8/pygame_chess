"""
this area is responsible for all the rendering methods
"""

from settings import *
from board import Board

class Game:

    def __init__(self):
        self.board = Board()

    # show methods
    def show_bg(self, surface):
        #draw the chess board 
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):

                if (row + col) % 2 == 0:
                    color = COLORS["beige"]
                else:
                    color = COLORS["green"]

                rect = (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)

                pygame.draw.rect(surface, color, rect)
                
                
    def show_pieces(self, surface):
        
        #draw the chess piece
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):

                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece
                    
                    img = pygame.image.load(piece.texture)
                    img_center = col * SQUARE_SIZE +SQUARE_SIZE // 2, row *SQUARE_SIZE + SQUARE_SIZE // 2
                    piece.texture_rect =  img.get_frect(center = img_center)
                    surface.blit(img,piece.texture_rect)
                    
                    

