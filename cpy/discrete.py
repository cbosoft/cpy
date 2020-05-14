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

    def ports(self):
        return {
                'left': (-2,0), 'right': (2,0)
            }

    def draw_value(self, *args):
        plt.text(self.x, self.y, self.value, ha='center', va='center')


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

    def ports(self):
        return {
                'left': (-1,0), 'right': (1,0)
            }
