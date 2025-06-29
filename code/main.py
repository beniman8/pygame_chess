from settings import *
from game import Game

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
        game = self.game
        
        while self.running:
            dt = self.clock.tick() / 1000
            
            game.show_bg(screen)
            game.show_pieces(screen)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    sys.exit()

            pygame.display.update()


if __name__ == "__main__":
    main = Main()
    main.mainloop()
