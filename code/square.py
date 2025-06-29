

class Square:
    '''
        This is a square that will contain our pieces
        depending on what row or column in the board array
    '''
    def __init__(self,row,col,piece=None):
        self.row = row 
        self.col = col 
        self.piece = piece
        
    def has_piece(self):
        # we are checking of the square already has a piece
        return self.piece != None