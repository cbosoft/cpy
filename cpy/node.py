from matplotlib import pyplot as plt

from cpy.util import rot


class Node:

    def __init__(self, x, y, rotation):
        self.x = x
        self.y = y
        self.angle = rotation
        self.plot_kws = {'color':'k'}

    def center(self):
        return self.x, self.y

    def data(self):
        return [self.x], [self.y]

    def draw(self):
        x, y = self.data()
        plt.plot(*rot(x, y, self.angle), **self.plot_kws)
