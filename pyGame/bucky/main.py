import pygame
import time
import random

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("THIS GAME")

display_width = 800
display_height = 600

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (34,177,76)
clock = pygame.time.Clock()

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 50)


def score(score):
    text = smallfont.render("Score: " + str(score), True, black)
    gameDistplay.blit(text, [0,0])

def text_objects(text, color, size ="small"):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()

def message_to_scree(msg, color, y_displace = 0, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (int(display_width/2, int(display_height/2)+y_displace))
    gameDisplace.blit(textSurf, textRect)

def pause():

    pause = True
    message_to_screen("Pause",black,-100,size="large")
    message_to_screen("Press C to continue playing or Q to quit",black,25)
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False
                    elif even.key == pygame.K_q:
                        pygame.quit()
                        quit()
        clock.tick(5)

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                intro = False
            elif event.key == pygame.K_q:
                
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        message_to_screen("WELCOME TO THE GAME", black, -100, size="large")
        message_to_screen("Press C to play, playing or Q to quit",black,25)
        pygame.display.update()

        clock.tick(15)

game_intro()

def gameLoop():
    gameExit = False
    gameOver = False
    FPS = 15

    while not gameExit:
        if gameOver == True:
            message_to_screen("Game Over", red,-50,size="large")
            message_to_screen("Press C to play, playing or Q to quit", red, 50,size="large")
            pygame.display.update()
            while gameOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False
                        
                    if event.type == pygame.KEYDOWN:
                        if event.type == pygame.K_c:
                            gameLoop()
                        elif event.type == pygame.K_q:
                            
                            gameExit = True
                            gameOver = False
            
        for event in pygame.event.get():
                     
            if event.type == pygame.QUIT:
                gameExit = True
                             
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pass
                elif event.key == pygame.K_RIGHT:
                    pass
                elif event.key == pygame.K_UP:
                    pass
                elif event.key == pygame.K_DOWN:
                    pass
                elif event.key == pygame.K_p:
                                pause()
                
       
            gameDisplay.fill(white)
               
            pygame.display.update()
            
            clock.tick(FPS)
    
    pygame.quit()
    quit()

gameLoop()
