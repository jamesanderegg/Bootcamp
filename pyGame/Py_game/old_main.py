import pygame
from Sprites import Rectangel, Ball, Customer
import random

#GLOBAL VARIABLES
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 900
R = 0
G = 30
B = 60

class Main_game():

    def __init__(self):

        #init everything in game
        
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

        self.game_running = True
        
        self.FPS = 30
        self.fps_numDays = 0
        self.rgb = [R,G,B]
        self.clock = pygame.time.Clock()
        self.playtime = 0
        self.numDays = 0
        self.ground_floor = 100
        self.day =True
        self.num_customers = 0
        
        #load everything
        self.sky = Rectangel()
        self.sky.width, self.sky.height = self.screen.get_size()
        self.sky.color = self.rgb

        self.ground = Rectangel()
        self.ground.width = SCREEN_WIDTH
        self.ground.height = self.ground_floor
        self.ground.color = [80,50,40]
        self.ground.y = SCREEN_HEIGHT - self.ground_floor

        self.customer_array = []
        
        self.customer_speed = 7
        
        
        self.play_game()
    def random_number(self,x):
        x = random.randint(0,x)
        return x
    def set_clock(self, playtime, fps, numDays):
        milliseconds = self.clock.tick(self.FPS)
        self.playtime += milliseconds / 1000.0
        text = "FPS: {0:.2f}   Playtime: {1:.2f}   Days: {2:0}".format(self.clock.get_fps(), self.playtime, self.numDays)
        return text, self.playtime

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
    def set_num_customers(self, x):
        #GENERATE RANDOM CUSTOMERS HERE
        
        self.num_customers = x
        return self.num_customers
        
    def sky_change(self):
        if self.day:
            
            if self.rgb[2] < 240:
                self.rgb[0] +=.5
                self.rgb[1] +=.5
                self.rgb[2] += .8
            else:
                self.day =False
                self.numDays +=.5
        else:
            if self.rgb[2] > 60:
                self.rgb[0] -=.5
                self.rgb[1] -=.5
                self.rgb[2] -= .8
            else:
                self.num_customers = 0
                self.day =True
                self.numDays +=.5
                self.customer_array[:] = []
    def morning_setup(self):
        self.num_customers = self.set_num_customers(self.random_number(50))
        print(self.num_customers)
        for i in range(self.num_customers):

            if i % 2 == 0:
                self.customer_array.append(Customer(self.random_number(100),(SCREEN_HEIGHT - self.ground_floor)- 30))
                self.customer_array[i].change_x = self.random_number(self.customer_speed)
                while self.customer_array[i].change_x < 3:
                    self.customer_array[i].change_x = self.random_number(self.customer_speed)
                    print(i)
            else:
                self.customer_array.append(Customer((self.random_number(100) + SCREEN_WIDTH-100),(SCREEN_HEIGHT - self.ground_floor)- 30))
                self.customer_array[i].change_x = (self.random_number(self.customer_speed)*-1)
                while self.customer_array[i].change_x > -3:
                    self.customer_array[i].change_x = (self.random_number(self.customer_speed)*-1)
                    print(i)
    def play_game(self):
    
        
        while self.game_running:
            self.fps_numDays, self.playtime = self.set_clock(self.playtime, self.FPS, self.numDays)
            self.game_running = self.check_quit()

            if(self.num_customers == 0):
                self.morning_setup()
            
            self.sky.draw(self.screen)
            self.sky_change()
            self.ground.draw(self.screen)
            for i in range(len(self.customer_array)):
                if(len(self.customer_array) != 0):
                    self.customer_array[i].draw(self.screen)
      

            pygame.display.set_caption(self.fps_numDays)
            pygame.display.update()
            
        pygame.quit()
