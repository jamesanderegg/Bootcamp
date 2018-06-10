import pygame
import random
from Sprites import Rectangel, Ball, Customer

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 900


class Main_game():

    def __init__ (self):
        pygame.init()
        
        self.window = Window()
        
        self.game_running = True
         
        self.play_game()
        
    def random_number(self,f,l):
        x = random.randint(f,l)
        return x

    
    def play_game(self):

        self.load_game()
        
        while self.game_running:
            self.game_running = self.window.check_quit()
            time_hours = self.window.set_clock()
            
            self.draw_game()
            
            pygame.display.set_caption(time_hours)
            pygame.display.update()
        pygame.quit()

    def draw_game(self):
        self.sky.draw(self.window.screen)
        

    def load_game(self):
        self.sky = Rectangel()
        self.sky.w, self.sky.h = self.window.screen.get_size()
        


        
class Window():
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playtime = 0
        self.FPS = 30
    def check_quit(self):
        for event in pygame.event.get():
        # User presses QUIT-button.
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
            # User presses ESCAPE-Key
                if event.key == pygame.K_ESCAPE:
                    self.game_running = False
                    return False
        return True

    def set_clock(self):
        milliseconds = self.clock.tick(self.FPS)
        self.playtime += milliseconds / 1000.0
        text = "FPS: {0:.2f}   HOURS: {1:.0f}".format(self.clock.get_fps(),
                                                                self.playtime)
        return text


    
