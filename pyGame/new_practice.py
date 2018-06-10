import pygame

pygame.init()

screen_height = 500
screen_width = 900
gameRunning = True

store_w = 200
store_h = 150

skyColor = (0,20,60)
rSky = 0
gSky = 20
bSky = 60
day = True

FPS = 30
playtime = 0
numDays = 1
clock = pygame.time.Clock()
class Sprite:

    def __init__(self,x,y):

        self.x =x
        self.y =y
        self.width =10
        self.height = 50
    def render(self):
        pygame.draw.rect(screen, (255,255,255),(self.x,self.y, self.width, self.height))


        
def create_surface(size):
    surface_name = pygame.Surface(size)
    return surface_name

def display_screen(screen_width,screen_height):
    display_screen = pygame.display.set_mode((screen_width,screen_height))
    return display_screen

def check_quit():
    for event in pygame.event.get():
        # User presses QUIT-button.
        if event.type == pygame.QUIT:
            
            return False
        elif event.type == pygame.KEYDOWN:
            # User presses ESCAPE-Key
            if event.key == pygame.K_ESCAPE:
               gameRunning = False
               return False
    return True
def blit_surface(surface,color, screen, location):
    surface.fill((color))
    surface = surface.convert()
    screen.blit(surface, (location))
def night_day(r,g,b, day, numDays):
    if day:
        if b <= 250:
            b += .5
            g += .6
            r += .5
        else:
            #print('DAy R', r, 'G ', g, 'B ', b)
            numDays +=.5
            day = False
    else:
        if b >= 60:
            b -= .5
            g -= .6
            r -= .5
        else:
            #print('NIGHT R', r, 'G ', g, 'B ', b)
            numDays +=.5
            day = True
    return r,g,b,day,numDays
def set_clock(playtime,fps, numdays):
    milliseconds = clock.tick(fps)
    playtime += milliseconds / 1000.0
    text = "FPS: {0:.2f}   Playtime: {1:.2f}   Days: {2:0}".format(clock.get_fps(), playtime, numDays)

    return text, playtime

#load window
screen = display_screen(screen_width,screen_height)

#load graphics
sky = create_surface(screen.get_size())
ground = create_surface((screen_width, screen_height-100))
store = create_surface((store_w,store_h))

#gameloop

player = Sprite(150,350)

while gameRunning:
    fps_numDays, playtime = set_clock(playtime, FPS,numDays)
    gameRunning = check_quit()

    #background
    blit_surface(sky,(rSky,gSky,bSky),screen, (0,0))
    blit_surface(ground,(100,60,0), screen, (0, screen_height - 100))
    rSky, gSky, bSky, day, numDays = night_day(rSky,gSky,bSky, day, numDays)
    #store
    blit_surface(store, (50,50,50),screen,((screen_width/2)-(store_w/2),(screen_height-100)-store_h))

    player.render()
    pygame.display.set_caption(fps_numDays)
    pygame.display.update()
    
pygame.quit()
