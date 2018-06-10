import pygame

class Rectangel():
    def __init__(self):

        #class atributes
        #position
        self.x= 0
        self.y=0
        self.w = 100
        self.h = 100
        self.c = [255,255,255]

        #class methods
    def draw(self, screen):
        pygame.draw.rect(screen,self.c, (self.x,self.y,self.w,self.h))

        
class Ball():
    def __init__(self):

        #class atributes
        #position
        self.x= 0
        self.y=0

        #radius
        self.r = 10
        self.c = [255,255,255]


        #class methods

    def move(self):
        self.x += self.change_x
        self.y += self.change_y

    def draw(self,screen):
        pygame.draw.circle(screen,self.color, (self.x,self.y),self.radius)

class Customer():
    def __init__(self):

        self.body = Rectangel()
        self.head = Ball()

        self.body.x = x_start
        self.body.y = y_start
        self.head.x = x_start
        self.head.y = y_start
        self.w = 11
        self.h = 30
        
        self.change_x =0
        self.change_y =0
       
 
        
    

    
