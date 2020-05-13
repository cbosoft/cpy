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
        pts = [
                (-1,1), (-1,-1), (np.nan, np.nan), (-1,0), (1,1), (1,-1), (-1,0), (np.nan,np.nan), (1, 0)
            ]
        return list(zip(*pts))

