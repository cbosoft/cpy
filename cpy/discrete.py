from matplotlib import pyplot as plt

from cpy.node import Node
from cpy.util import null, trf


class Resistor(Node):

    def data(self):

        return [
                (-1.5,0.5),
                (1.5,0.5),
                (1.5,-0.5),
                (-1.5,-0.5),
                (-1.5,0.5),
                null,
                (-1.5,0), (-2,0),
                null,
                (1.5,0), (2,0),
                null
            ]

    def draw_value(self, *args):
        plt.text(self.x, self.y, self.value, ha='center', va='center')

    def left(self):
        return self.x-2, self.y

    def right(self):
        return self.x+2, self.y

class Capacitor(Node):

    def data(self):

        return [
                (-0.5,1),
                (-0.5,-1),
                null,
                (0.5,1),
                (0.5,-1),
                null,
                (0.5,0), (1.0,0),
                null,
                (-0.5,0), (-1.0,0),
                null
            ]

    def left(self):
        return self.x-1, self.y

    def right(self):
        return self.x+1, self.y
