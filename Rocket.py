import numpy as np
import pygame
import Constants
import DNA
from pygame.locals import *


class Rocket:
    def __init__(self, dna=None):
        self.pos = np.asarray([Constants.width / 2, Constants.height - 20])
        self.vel = np.asarray([0.0, 0.0])
        self.acc = np.asarray([0.0, 0.0])
        self.surface = pygame.Surface((5, 5), SRCALPHA)
        self.surface.fill(Constants.White)

        Constants.count = 0
        self.crashed = False
        self.completed = False
        self.time = 0
        self.fitness = 0

        if (dna):
            self.dna = dna
        else:
            self.dna = DNA.DNA()

    def applyForce(self, force):
        self.acc += force

    def calcFitness(self):
        dist = self.calcDist(Constants.target)
        # print("goal",Constants.goaldistance)
        #dist = (Constants.goaldistance - dist)/2
        dist = 1000/dist
        # if dist < 0:
        #     dist = 0
        #time = (self.time/2)**2
        time = self.time*10
        if self.completed:
            #self.fitness = (dist + time)
            self.fitness = (time)/dist
        elif self.crashed:
            self.fitness = dist**0.5
        else:
            self.fitness = dist

        #print("fitness", self.fitness, "dist ", dist, "time ", time)

    def update(self):

        if not self.crashed:
            if self.pos[0] > Constants.width or self.pos[0] < 0:
                self.crashed = True
                self.surface.fill(Constants.Red)

            if self.pos[1] > Constants.height or self.pos[1] < 0:
                self.crashed = True
                self.surface.fill(Constants.Red)


        if not self.completed:
            if self.calcDist(Constants.target) <= 15 and self.completed is False:
                self.time = Constants.lifespan - Constants.count
                self.completed = True
                self.surface.fill(Constants.Green)

                # print("time",self.time)

        self.applyForce(self.dna.a[Constants.count])
        if not self.completed and not self.crashed:
            self.vel += self.acc
            self.pos += self.vel
            self.acc = self.acc.__mul__(0)
            self.limit()

    def display(self):
        self.rotated_surface = pygame.transform.rotate(self.surface, self.rotate())
        self.rect = self.rotated_surface.get_rect(center=self.pos)
        Constants.screen.blit(self.rotated_surface, (self.rect.x, self.rect.y))

    def rotate(self):
        angle = np.arctan2(self.vel[0], self.vel[1])
        return (angle * (180 / np.pi))

    def limit(self):
        if self.vel[0] > 4:
            self.vel[0] = 4
        if self.vel[0] < -4:
            self.vel[0] = -4
        if self.vel[1] > 4:
            self.vel[1] = 4
        if self.vel[1] < -4:
            self.vel[1] = -4

    def calcDist(self, target):
        distance = np.linalg.norm(self.pos - target)
        return distance

