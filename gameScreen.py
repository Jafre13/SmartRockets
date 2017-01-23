import pygame
import Constants
import Rocket
import Population
import numpy as np
pygame.init()


pygame.display.set_caption("Smart Rockets")
population = Population.Population()
clock = pygame.time.Clock()
running = True

myfont = pygame.font.SysFont("monospace", 20)

def update():
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            global running
            running = False# Flag that we are done so we exit this loop




def draw():

    Constants.screen.fill(Constants.Black)
    pygame.draw.circle(Constants.screen,Constants.White,Constants.target,15)
    label1 = myfont.render("MaxFitness "+str(Constants.MaxFit),1,Constants.White)
    label2 = myfont.render("Generation "+str(Constants.Generation),1,Constants.White)
    Constants.screen.blit(label1,(100,100))
    Constants.screen.blit(label2,(100,150))
    population.run()

    Constants.count += 1

    if Constants.count == Constants.lifespan:
        population.evaluate()
        population.selection()
        Constants.count = 0

    pygame.display.flip()




while running:
    update()
    draw()
    clock.tick(60)



pygame.quit()