#!/bin/env python

import matplotlib.pyplot as plt
import numpy as np


class PrimeGraph:

    def __init__(self):
        plt.figure()

    def loadFromFile(self, infilename):
        data = np.genfromtxt(infilename, delimiter=',', names=True)
        self.xs = data[data.dtype.names[0]]
        self.ys = data[data.dtype.names[1]]
        self.xlabel = data.dtype.names[0]
        self.ylabel = data.dtype.names[1]
        # plt.rc('text', usetex=True)

    def graphPlot(self):
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)

        plt.plot(self.xs, self.ys, label=self.ylabel)
        plt.legend()

    def display(self):
        plt.show()

    def calculateSlopes(self):
        self.ys = self.ys/self.xs

    def graphSave(self, fileName, xaxis, yaxis, title):
        fig = plt.figure()
        ax = fig.add_subplot(111)

        ax.set_title(title)
        ax.set_xlabel(xaxis)
        ax.set_ylabel(yaxis)

        ax.plot(self.xs, self.ys)
        plt.savefig(fileName)

primeGraph = PrimeGraph()
for i in range(1, 5):
    primeGraph.loadFromFile("run" + str(i) + ".txt")
    primeGraph.calculateSlopes()
    primeGraph.graphPlot()
primeGraph.display()
