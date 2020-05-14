import numpy as np

from cpy.util import null
from cpy.node import Node
from cpy.tikz import pts2path

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

    def paths(self):

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

        paths = [pts2path(pts)]
        paths.append(f'\\draw ({-h-t},0.2) arc(90:-90:0.2);')
        return paths


class DIP6(DIPn):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, n=6)
