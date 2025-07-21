from settings import *
from game import Game
from square import Square
from move import Move
class Main:
    
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption('CHESS')
        self.game =Game()
        
        self.clock = pygame.time.Clock()
        self.running = True 
    
    def mainloop(self):
        
        screen = self.display_surface
        board = self.game.board
        game = self.game
        dragger = self.game.dragger
        
        while self.running:
            #show methods
            game.show_bg(screen)
            game.show_last_move(screen)
            game.show_moves(screen)
            game.show_pieces(screen)
            
            game.show_hover(screen)
            
            if dragger.dragging:
                dragger.update_blit(screen)
            
            for event in pygame.event.get():
                
                # click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    
                    
                    clicked_row = dragger.mouseY // SQUARE_SIZE
                    clicked_col = dragger.mouseX // SQUARE_SIZE
                    
                    # if clicked square has a piece
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        #valid piece color 
                        if piece.color == game.next_player:
                            board.calc_moves(piece,clicked_row,clicked_col,bool=True)
                            dragger.save_initial(event.pos)
                            dragger.drag_piece(piece)
                            
                            #show methods 
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            
                            game.show_moves(screen)
                            
                            game.show_pieces(screen)
                        
                    
                
                # mouse motion
                if event.type == pygame.MOUSEMOTION:
                    motion_row =event.pos[1] // SQUARE_SIZE
                    motion_col = event.pos[0] // SQUARE_SIZE
                    game.set_hover(motion_row,motion_col)
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        #show methods
                        game.show_bg(screen)
                        game.show_last_move(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        game.show_hover(screen)
                        dragger.update_blit(screen)
                
                # click release
                elif event.type == pygame.MOUSEBUTTONUP:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        release_row = dragger.mouseY // SQUARE_SIZE
                        release_col = dragger.mouseX // SQUARE_SIZE
                        
                        
                        #create possible move 
                        initial = Square(dragger.initial_row,dragger.initial_col)
                        final = Square(release_row,release_col)
                        move = Move(initial,final)
                        
                        
                        # valid move ?
                        if board.valid_move(dragger.piece,move):
                            #normal capture
                            captured = board.squares[release_row][release_col].has_piece()
                            board.move(dragger.piece,move)
                            board.set_true_en_passant(dragger.piece)
                            #sounds
                            game.play_sound(captured)
                            #show methods
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_pieces(screen)
                            
                            # next turn 
                            
                            game.next_turn()
                            
                        
                    dragger.undrag_piece()
                #key press
                
                elif event.type == pygame.KEYDOWN:
                    
                    #changing theme
                    if event.key == pygame.K_t:
                        game.change_theme()
                    #restart game
                    if event.key == pygame.K_r:
                        game.reset()
                        game = self.game
                        board = self.game.board
                        dragger = self.game.dragger
                        
                        
                # quite the application
                elif event.type == pygame.QUIT:
                    self.running = False
                    sys.exit()

            pygame.display.update()


if __name__ == "__main__":
    main = Main()
    main.mainloop()
