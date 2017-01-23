import numpy as np
import Rocket
import Constants

class Population:
    def __init__(self):
        self.rockets = []
        self.popsize = Constants.popsize
        self.matingpool = []
        for i in range(self.popsize):
            self.rockets.append(Rocket.Rocket())

    def evaluate(self):
        maxfit = 0
        for i in range(self.popsize):
            self.rockets[i].calcFitness()
            if self.rockets[i].fitness > maxfit:
                maxfit = self.rockets[i].fitness

        for i in range(self.popsize):
            self.rockets[i].fitness /= maxfit+1

        self.matingpool = []
        for i in range(self.popsize):
            n = self.rockets[i].fitness*100
            for j in range(int(n)):
                self.matingpool.append(self.rockets[i])

        Constants.MaxFit = maxfit

    def selection(self):
        newRockets = []
        dif = False
        for i in range(self.popsize):
            while not dif:
                parentA = np.random.choice(self.matingpool).dna
                parentB = np.random.choice(self.matingpool).dna
                if parentA != parentB:
                    dif = True
            child = parentA.crossover(parentB)
            child.mutation()
            newRockets.append(Rocket.Rocket(dna = child))
        self.rockets = newRockets
        Constants.Generation+=1

    def run(self):
        for i in range(self.popsize):
            self.rockets[i].update()
            self.rockets[i].display()




