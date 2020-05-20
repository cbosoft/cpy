import numpy as np

from cpy.util import null
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

    def paths(self):

        h = (self.n-1)/2
        yb = self.w/2
        t = 0.5

        paths = [f'\\draw ({-h-t},{yb}) rectangle ({h+t},{-yb});']

        for i in range(self.n):
            paths.append(f'\\draw ({-h+i}, {yb}) -- ++ (0, 0.5);')
            paths.append(f'\\draw ({-h+i},{-yb}) -- ++ (0,-0.5);')

        if self.draw_semicircle:
            paths.append(f'\\draw ({-h-t},0.2) arc(90:-90:0.2);')
        return paths


class DIP6(DIPn):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, n=6)
