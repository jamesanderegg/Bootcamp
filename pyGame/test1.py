import pygame

# Initialize Pygame.
pygame.init()
# Set size of pygame window.
screen=pygame.display.set_mode((630,480))
# Create empty pygame surface.
background = pygame.Surface(screen.get_size())
# Fill the background white color.
background.fill((255, 255, 255))
# Convert Surface object to make blitting faster.
background = background.convert()
# create a rectangular surface for the ball
ballsurface = pygame.Surface((50,50))
# draw blue filled circle on ball surface
pygame.draw.circle(ballsurface, (0,0,255), (0,0),25)
ballsurface = ballsurface.convert() 
ballx = 50
bally = 50

# pygame.draw.rect(Surface, color, Rect, width=0): return Rect
# rect: (x-position of topleft corner, y-position of topleft corner, width, height)
pygame.draw.rect(background, (0,255,0), (50,50,100,25))
# pygame.draw.circle(Surface, color, pos, radius, width=0): return Rect
pygame.draw.circle(background, (0,200,0), (200,50), 35)
# pygame.draw.polygon(Surface, color, pointlist, width=0): return Rect
pygame.draw.polygon(background, (0,180,0), ((250,100),(300,0),(350,50)))
# pygame.draw.arc(Surface, color, Rect, start_angle, stop_angle, width=1): return Rect
# radiant instead of grad
pygame.draw.arc(background, (0,150,0),(400,10,150,100), 0, 3.14) 

#---
# Copy background to screen (position (0, 0) is upper left corner).
screen.blit(background, (0,0))
# blit the topleft corner of ball surface at pos (ballx, bally)
screen.blit(ballsurface, (ballx, bally))  
# Create Pygame clock object.  
clock = pygame.time.Clock()

mainloop = True
# Desired framerate in frames per second. Try out other values.              
FPS = 30
# How many seconds the "game" is played.
playtime = 0

while mainloop:
    # Do not go faster than this framerate.
    milliseconds = clock.tick(FPS) 
    playtime += milliseconds / 1000.0 
    
    for event in pygame.event.get():
        # User presses QUIT-button.
        if event.type == pygame.QUIT:
            mainloop = False 
        elif event.type == pygame.KEYDOWN:
            # User presses ESCAPE-Key
            if event.key == pygame.K_ESCAPE:
                mainloop = False
                
    # Print framerate and playtime in titlebar.
    text = "FPS: {0:.2f}   Playtime: {1:.2f}".format(clock.get_fps(), playtime)
    pygame.display.set_caption(text)

    #Update Pygame display.
    pygame.display.flip()

# Finish Pygame.  
pygame.quit()

