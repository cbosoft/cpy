import numpy as np

from cpy.node import Node

class Diode(Node):

    def __init__(self, x, y, rotation=0):
        super().__init__(x, y, rotation)

    def anode(self):
        return self.x+1, self.y

    def cathode(self):
        return self.x-1, self.y

    def data(self):
        return [
                null,
                (-1,1),
                (-1,-1),
                null,
                (-1,0),
                (1,1),
                (1,-1),
                (-1,0),
                null,
                (1, 0),
                (1.5,0),
                null,
                (-1.0,0),
                (-1.5,0),
                null
            ]

