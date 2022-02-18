import pygame
import random
pygame.init


#creates game screen and caption
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("simple base code")

#game variables
doExit = False #variable to quit out of game loop

clock = pygame.time.Clock()

class butter():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def draw(self):
        pygame.draw.circle(screen, (255, 0, 255), (self.x, self.y), 35)

        pygame.draw.circle(screen, (255, 75, 255), (self.x,self.y-20), 35)

        pygame.draw.circle(screen, (255, 0, 255), (self.x+50, self.y), 35)

        pygame.draw.circle(screen, (255, 75, 255), (self.x+50, self.y-20), 35)

        pygame.draw.ellipse(screen,(255,255,0),(self.x+10, self.y-60, 30, 100), 0)

        pygame.draw.line(screen, (0, 0, 0), (self.x+10, self.y-80), (self.x+20, self.y-40), 5)

        pygame.draw.line(screen, (0, 0, 0), (self.x+40, self.y-80), (self.x+30, self.y-40), 5)

        pygame.draw.arc(screen, (255, 200, 0), (self.x+5, self.y-70, 40, 40), 5*3.14/4, 7*3.14/4,5)

        pygame.draw.arc(screen, (255, 200, 0), (self.x+5, self.y-50, 40, 40), 5*3.14/4, 7*3.14/4,5)

        pygame.draw.arc(screen, (255, 200, 0), (self.x+5, self.y-30, 40, 40), 5*3.14/4, 7*3.14/4,5)

        pygame.draw.arc(screen, (255, 200, 0), (self.x+5, self.y-10, 40, 40), 5*3.14/4, 7*3.14/4,5)

butterfly = list()
for i in range(8):
    butterfly.append(butter(random.randrange(100,700),random.randrange(100,700)))

#BEGIN GAME LOOP######################################################
while not doExit:
   
    clock.tick(60) #FPS (frames per second)
   
    #pygame's way of listening for events (key presses, mouse clicks, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           doExit = True #lets you quit program

  
    #render section-----------------------------------
    screen.fill((0,255,255))

    
     

    for butter in butterfly:
        butter.draw()

    pygame.draw.line


    pygame.display.flip() #update graphics each game loop

#END GAME LOOP#######################################################
pygame.quit()
