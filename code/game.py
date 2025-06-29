"""
this area is responsible for all the rendering methods
"""

from settings import *
from board import Board
from dragger import Dragger
class Game:

    def __init__(self):
        
        #create a board
        self.board = Board()
        self.dragger = Dragger()

    # show methods
    def show_bg(self, surface):
        #draw the chess board 
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):

                if (row + col) % 2 == 0:
                    color = COLORS["beige"]
                else:
                    color = COLORS["green"]
                # creating a rect depending on the square size we specify
                rect = (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                # we draw a rect 
                pygame.draw.rect(surface, color, rect)
                
                
    def show_pieces(self, surface):
        
        #draw the chess piece
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):

                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece
                    
                    # all pieces except dragger piece
                    if piece is not self.dragger.piece:
                        piece.set_texture(size=80)
                        img = pygame.image.load(piece.texture)
                        img_center = col * SQUARE_SIZE +SQUARE_SIZE // 2, row *SQUARE_SIZE + SQUARE_SIZE // 2
                        piece.texture_rect =  img.get_frect(center = img_center)
                        surface.blit(img,piece.texture_rect)
                    
                    

