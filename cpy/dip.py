import numpy as np
from matplotlib import pyplot as plt

from cpy.util import trf, null, arc
from cpy.node import Node

class DIPn(Node):

    def __init__(self, x, y, n=1, **kwargs):
        super().__init__(x, y, **kwargs)
        self.n = n

    def port(self, index):

        h = (self.n-1)/2
        x = -h+index

        if index > (self.n-1):
            y = 1.5
        else:
            y = -1.5

        return x,y

    def ports(self):

        return [self.port(i) for i in range(2*self.n)]

    def data(self):

        h = (self.n-1)/2
        t = 0.5

        pts = [
                (-h,1),(-h-t,1),(-h-t,-1),(-h,-1),
                (h,-1),(h+t,-1),(h+t,1),(h,1),(-h,1)
            ]

        for i in range(self.n):
            pts.extend([
                null,
                (-h + i, 1), (-h + i, 1.5),
                null,
                ])
            pts.extend([
                null,
                (-h + i, -1), (-h + i, -1.5),
                null,
                ])

        pts.extend(zip(*arc( (-h-t,0), 0.2, 0, -180)))

        return pts

    def draw_label(self, *args):
        plt.text(self.x, self.y, self.label, ha='center', va='center')


class DIP6(DIPn):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, n=6)
