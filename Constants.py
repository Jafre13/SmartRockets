import pygame
import numpy as np
#Colors
Black = (0,0,0)
White = (255,255,255)
Blue = (0,0,255)

#Game constants
width = 800
height = 600
size = (width,height)
screen = pygame.display.set_mode(size)
target = np.asarray([int(width/2),50])
start = np.asarray([int(width/2),height-50])
count = 0
goaldistance = np.linalg.norm(target-start)

#GA
lifespan = 300
popsize = 25
mutationRate = 0.05


#GUI
Generation = 0
MaxFit =0