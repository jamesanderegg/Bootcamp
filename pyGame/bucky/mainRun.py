#Load and initialize Modules here
import pygame
pygame.init()

#Window Information
displayw = 800
displayh = 600
window = pygame.display.set_mode((displayw,displayh))

#Clock
windowclock = pygame.time.Clock()

#Load other things such as images and sound files here
image = pygame.image.load("foo.png").convert #Use conver_alpha() for images with transparency

#Main Class
class MainRun(object):
    def __init__(self,displayw,displayh):
        self.dw = displayw
        self.dh = displayh
        self.Main()

    def Main(self):
        #Put all variables up here
        stopped = False

        while stopped == False:
            window.fill((255,255,255)) #Tuple for filling display... Current is white

            #Event Tasking
            #Add all your event tasking things here
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    stopped = True

            #Add things like player updates here
            #Also things like score updates or drawing additional items
            #Remember things on top get done first so they will update in the order yours is set at

            #Remember to update your clock and display at the end
            pygame.display.update()
            windowclock.tick(60)

        #If you need to reset variables here
        #This includes things like score resets

    #After your main loop throw in extra things such as a main menu or a pause menu
    #Make sure you throw them in your main loop somewhere where they can be activated by the user

#All player classes and object classes should be made outside of the main class and called inside the class
#The end of your code should look something like this
