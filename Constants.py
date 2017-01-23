import pygame
import numpy as np
#Colors
Black = (0,0,0)
White = (255,255,255)
Blue = (0,0,255)
Red = (255,0,0)
Green = (0,255,0)

#Game constants
width = 1200
height = 800
size = (width,height)
screen = pygame.display.set_mode(size)
target = np.asarray([int(width/2),50])
start = np.asarray([int(width/2),height-50])
count = 0
goaldistance = np.linalg.norm(target-start)

#GA
lifespan = 300
popsize = 100
mutationRate = 0.01


#GUI
Generation = 0
MaxFit =0