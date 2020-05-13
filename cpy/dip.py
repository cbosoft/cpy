import numpy as np

from cpy.util import trf, null
from cpy.node import Node

class DIPn(Node):

    def __init__(self, x, y, rotation=0, n=1):
        super().__init__(x, y, rotation)
        self.n = n

    def port(self, index):

        h = (self.n-1)/2
        x = -h+index

        if index > (self.n-1):
            y = 1.5
        else:
            y = -1.5

        return x+self.x,y+self.y

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

        ll = -h-t
        r=0.2
        hcx = np.linspace(0.0,0.25)
        hcy = np.sqrt(np.subtract(np.power(r, 2.0), np.power(hcx, 2.0)))

        for cx, cy in zip(hcx, hcy):
            pts.append([cx+ll, cy])
        for cx, cy in zip(hcx, hcy):
            pts.append([cx+ll,-cy])

        x, y = zip(*pts)

        return trf(x, y, self.x, self.y)

class DIP6(DIPn):

    def __init__(self, x, y, rotation=0):
        super().__init__(x, y, rotation=0, n=6)
