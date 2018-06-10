import pygame
import random

from Sprites import Rectangel, Ball, Customer

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 900
R = 0
G = 30
B = 60
GROUND = 100
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

class Main_game():

    def __init__ (self):
        pygame.init()
        self.window = Window()
        self.rgb = [R,G,B]
        self.game_running = True

        self.hours = 0
        self.days = 0
        self.time_speed = [0,0,0]
        
        self.load_game()
        self.play_game()
        
    def text_objects(self,text, font):
        textSurface = font.render(text, True, WHITE)
        return textSurface, textSurface.get_rect()

    def message_display(self,text):
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = self.text_objects(text, largeText)
        TextRect.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
        self.window.screen.blit(TextSurf, TextRect)

        pygame.display.update()

        

            
    def random_number(self,f,l):
        x = random.randint(f,l)
        return x
    
    def play_game(self):
  
        while self.game_running:
            self.game_running = self.window.check_quit()
            seconds, self.playtime = self.window.set_clock()
            
            self.draw_game(self.window.screen)

            
            self.button("HELLO", 100,100,100,100, WHITE, RED,self.hi)
            self.message_display(str(self.playtime))            
            self.days = self.keep_time(self.playtime /2)
            
            pygame.display.set_caption(seconds)
            pygame.display.update()
        pygame.quit()
    def hi(self):
        print("hi")
    def draw_game(self, surface):
        self.sky.draw(surface)
        self.ground.draw(surface)

    def load_game(self):
        self.sky = Rectangel()
        self.sky.w, self.sky.h = self.window.screen.get_size()
        self.sky.c = self.rgb

        self.ground = Rectangel()
        self.ground.w = SCREEN_WIDTH
        self.ground.h = GROUND
        self.ground.c = [80,50,40]
        self.ground.y = SCREEN_HEIGHT - GROUND

    def keep_time(self, hours):
        self.hours = hours
        
        if ((self.hours / 12) % 1) == 0:
            self.days = self.hours / 12
           
        return self.days

    def button(self,msg,x,y,w,h,ic,ac,action=None):
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            
            if x+w > mouse[0] > x and y+h > mouse[1] > y:
                pygame.draw.rect(self.window.screen, ac,(x,y,w,h))
                if click[0] == 1 and action != None:
                    
                    action()
            else:
                pygame.draw.rect(self.window.screen, ic,(x,y,w,h))

            smallText = pygame.font.Font("freesansbold.ttf",20)
            textSurf, textRect = self.text_objects(msg, smallText)
            textRect.center = ( (x+(w/2)), (y+(h/2)) )
            self.window.screen.blit(textSurf, textRect)
    #def change_speed(self, x):
        
            
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
        text = "FPS: {0:.2f}   Seconds: {1:.0f}".format(self.clock.get_fps(),
                                                       self.playtime)
        x= "{0:.0f}".format(self.playtime)
        x = float(x)
        return text, x


    
