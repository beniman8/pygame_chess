

class Square:
    '''
        This is a square that will contain our pieces
        depending on what row or column in the board array
    '''
    ALPHACOLS={0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',}
    def __init__(self,row,col,piece=None):
        self.row = row 
        self.col = col 
        self.piece = piece
        self.alphacol = self.ALPHACOLS[col]
        
    def __eq__(self, other):
        return self.row == other.row and self.col == other.col
        
    def has_piece(self):
        # we are checking of the square already has a piece
        return self.piece != None
    
    def isempty(self):
        '''check if the square is empty'''
        return not self.has_piece()
    
    def has_team_piece(self,color):
        ''' return if the square has a piece in it and that the color is the same as the one we currently selected'''
        return self.has_piece() and self.piece.color ==color    
    
    def has_enemy_piece(self,color):
        ''' return if the square has a piece in it and that the color is different than the one we currently selected'''
        return self.has_piece() and self.piece.color !=color    
    def isempty_or_enemy(self,color):
        return self.isempty() or self.has_enemy_piece(color)
    
    @staticmethod
    def in_range(*args):
        for arg in args:
            if arg <0 or arg >7:
                return False
            
        return True
    
    @staticmethod
    def get_alphacol(col):
        ALPHACOLS={0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',}
        return ALPHACOLS[col]
        