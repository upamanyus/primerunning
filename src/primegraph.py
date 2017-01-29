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

    def loadAllFromFile(self, infilename):
        data = np.genfromtxt(infilename, delimiter=',', names=True)
        self.xlabel = data.dtype.names[0]
        self.xs = data[data.dtype.names[0]]
        self.yss = []
        self.ylabels = []
        for name in data.dtype.names[1:]:
            self.yss.append(data[name])
            self.ylabels.append(name)

    def graphPlotAll(self):
        plt.xlabel(self.xlabel)
        plt.ylim(0.8/len(self.yss), 1.5/len(self.yss))

        for i in range(len(self.yss)):
            plt.plot(self.xs, self.yss[i], label=self.ylabels[i])
            plt.legend()

    def graphPlot(self):
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)

        plt.plot(self.xs, self.ys, label=self.ylabel)
        plt.legend()


    def display(self):
        plt.show()

    def calculateSlopes(self):
        self.ys = self.ys/self.xs

    def calculateSlopesAll(self):
        for i in range(len(self.yss)):
            self.yss[i] = self.yss[i]/self.xs

    def graphSave(self, fileName, xaxis, yaxis, title):
        fig = plt.figure()
        ax = fig.add_subplot(111)

        ax.set_title(title)
        ax.set_xlabel(xaxis)
        ax.set_ylabel(yaxis)

        ax.plot(self.xs, self.ys)
        plt.savefig(fileName)

primeGraph = PrimeGraph()
primeGraph.loadAllFromFile('out.txt')
primeGraph.calculateSlopesAll()
primeGraph.graphPlotAll()
primeGraph.display()
