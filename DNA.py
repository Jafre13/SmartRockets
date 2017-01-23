import numpy as np

import Constants


class DNA:
    def __init__(self,genes = None):

        if (genes):
            self.a = genes
        else:
            self.a = [None]*Constants.lifespan
            self.fill()

    def fill(self):
        for i in range (0,len(self.a)):
            unit = self.getUnitVector(np.asarray([np.random.uniform(-1, 1), np.random.uniform(-1, 1)]))
            self.a[i] = unit

    def getUnitVector(self,vector,scale=1):
        mag = [np.sqrt(vector[0]**2+vector[1]**2)]
        unit = vector/mag
        return unit


    def crossover(self,partner):
        newGenes = []
        for i in range(len(self.a)):
            if np.random.uniform()<=0.5:
                newGenes.append(self.a[i])
            else:
                newGenes.append(partner.a[i])
        return DNA(newGenes)

    def mutation(self):
        for i in range(len(self.a)):
            if np.random.random_sample() <= Constants.mutationRate:
                self.a[i] =  [np.random.uniform(-1,1),np.random.uniform(-1,1)]
