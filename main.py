import sys
import pygame
from lib.base import Base
import lib.core

class Game(Base):

    screen = False
    game_state = lib.core.GameState.MENU

    def __init__(self):
        Base.__init__(self)
        pygame.init()
        self.screen = pygame.display.set_mode([1024, 768])

    def main_loop(self):
        while 1:
            for event in pygame.event.get():
                self.handle_core_events(event)   
        
            if(self.game_state == lib.core.GameState.MENU):
                self.show_menu()
            else:      
                self.screen.fill(self.COLOR_BLACK)
                pygame.display.flip()

    def show_menu(self):
        import screens.menu
        menu = screens.menu.MainMenu()
        menu.draw_background(self.screen)
        pass


# Game entry point!
g = Game()
g.main_loop()