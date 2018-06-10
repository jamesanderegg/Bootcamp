import pygame

pygame.init()

screen_height = 500
screen_width = 900

clock = pygame.time.Clock()
FPS = 30
playtime = 0

screen = pygame.display.set_mode((screen_width,screen_height))

sky = pygame.Surface(screen.get_size())
ground = pygame.Surface((screen_width, 100))

day = True
numDays = 0
gameRunning = True

r = 0
g = 20
b = 60

#106, 162, 252

while gameRunning:
    milliseconds = clock.tick(FPS)
    playtime += milliseconds / 1000.0
    print(playtime)
    for event in pygame.event.get():
        # User presses QUIT-button.
        if event.type == pygame.QUIT:
            gameRunning = False 
        elif event.type == pygame.KEYDOWN:
            # User presses ESCAPE-Key
            if event.key == pygame.K_ESCAPE:
               gameRunning = False

    if day:
        if b <= 250:
            b += .5
            g += .6
            r += .5
        else:
            #print('DAy R', r, 'G ', g, 'B ', b)
            day = False
    else:
        if b >= 60:
            b -= .5
            g -= .6
            r -= .5
        else:
            #print('NIGHT R', r, 'G ', g, 'B ', b)
            numDays +=1
            day = True
    
    sky.fill((r,g,b))
    sky = sky.convert()
    ground.fill((100,60,0))
    ground = ground.convert()
    screen.blit(sky, (0,0))
    screen.blit(ground, (0,screen_height - 100))
    
    text = "FPS: {0:.2f}   Playtime: {1:.2f}   Days: {2:0}".format(clock.get_fps(), playtime, numDays)
    pygame.display.set_caption(text)
    pygame.display.update()
    
pygame.quit()
