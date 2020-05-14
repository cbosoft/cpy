from matplotlib import pyplot as plt

from cpy.util import trf, null, arrow, circle
from cpy.node import Node

class TransistorNPN(Node):

    def data(self):

        return [
                null,
                (1, 2),
                (1, 1.5),
                (0,0.5),
                null,
                (-0.05,1),
                (-0.05,-1),
                null,
                (0,1),
                (0,-1),
                null,
                *arrow( (0,-0.5), end=(1,-1.5), inline=True),
                (1,-2),
                null,
                (0,0),
                (-0.5,0)
            ]

    def base(self):
        return self.trot(-0.5, 0)

    def collector(self):
        return self.trot(1, 2)

    def emitter(self):
        return self.trot(1, -2)

    def ports(self):
        return {
                'base': (-0.5, 0),
                'collector': (1,2),
                'emitter': (1,-2)
            }

    def draw_label(self, *args):
        plt.text(self.x+1.1, self.y+0.4, self.label, ha='center', va='center')

    def draw_value(self, *args):
        plt.text(self.x+1.1, self.y-0.4, self.value, ha='center', va='center')


class TransistorPNP(TransistorNPN):

    def data(self):
        return [
                null,
                (1, 2),
                *arrow( (1,1.5), end=(0,0.5), inline=True),
                null,
                (0,1),
                (0,-1),
                null,
                (-0.05,1),
                (-0.05,-1),
                null,
                (1, -2),
                (1, -1.5),
                (0, -0.5),
                null,
                (0,0),
                (-0.5,0)
            ]


class PhotoTransistor(TransistorNPN):

    def data(self):

        return [
                null,
                (1, 2),
                (1, 1.5),
                (0,0.5),
                null,
                (-0.05,1),
                (-0.05,-1),
                null,
                (0,1),
                (0,-1),
                null,
                *arrow( (0,-0.5), end=(1,-1.5), inline=True),
                (1,-2),
                null,
                *circle( (0.5,0), 1.7),
                *arrow( (-0.9, 1.5), length=1.0, rotation=45, backwards=True),
                *arrow( (-1.2, 1.2), length=1.0, rotation=45, backwards=True),
            ]
