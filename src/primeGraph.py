import matplotlib.pyplot as plt
import numpy as np
from pylab import figure
class primeGraph:

    def __init__(self, textName):
        self.data = np.genfromtxt(textName, delimiter = ',',
                names=['x','y'])
        
    def graphShow(self, xaxis, yaxis, title):
        fig = plt.figure()
        ax = fig.add_subplot(111)

        ax.set_title(title)
        ax.set_xlabel(xaxis)
        ax.set_ylabel(yaxis)
        
        ax.plot(self.data['x'], self.data['y'])
        plt.show()

    def graphSave(self,fileName, xaxis, yaxis, title):
        fig = plt.figure()
        ax = fig.add_subplot(111)

        ax.set_title(title)
        ax.set_xlabel(xaxis)
        ax.set_ylabel(yaxis)
        
        ax.plot(self.data['x'], self.data['y'])
        plt.savefig(fileName)
