from settings import *
from square import Square
from piece import *



class Board:
    
    def __init__(self):
        #the chess squares represented in a 2 dimension arrays containing zeros
        self.squares =[[0,0,0,0,0,0,0,0] for col in range(BOARD_COLS)]
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')
        
    
    
    def _create(self):
        #we are going through all the rows and column of the board
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                # we are creating squares depending on the row and column in the array
                self.squares[row][col] = Square(row,col)

    def _add_pieces(self,color):
        #placing the pawns on their respective rows depending on their colors
        row_pawn,row_other = (6,7) if color == 'white' else (1,0)
        
        # pawns
        for col in range(BOARD_COLS):
            self.squares[row_pawn][col] = Square(row_pawn,col,Pawn(color))
            
        # knights
        self.squares[row_other][1] = Square(row_other,1,Knight(color))
        self.squares[row_other][6] = Square(row_other,6,Knight(color))
        
        # bishops
        self.squares[row_other][2] = Square(row_other,2,Bishop(color))
        self.squares[row_other][5] = Square(row_other,5,Bishop(color))
        
        # rooks
        self.squares[row_other][0] = Square(row_other,0,Rook(color))
        self.squares[row_other][7] = Square(row_other,7,Rook(color))
        
        # queen
        self.squares[row_other][3] = Square(row_other,3,Queen(color))

        # king
        self.squares[row_other][4] = Square(row_other,4,King(color))

        
        
            