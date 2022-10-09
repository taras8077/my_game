import pygame
from pygame.locals import*
pygame.init()
import sys
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
FPSclock=pygame.time.Clock
fps=60
width,hight=640,480
screen=pygame.display.set_mode((width,height))
While True:
    screen.feel((0,0,0))
    for event in pygame.event_get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    FPSclock.tick(fps)
