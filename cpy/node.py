import numpy as np
from matplotlib import pyplot as plt

from cpy.util import rot, trf, null


class Node:

    def __init__(self, x, y, rotation=0, label=None, value=None):
        self.x = x
        self.y = y
        self.angle = rotation
        self.plot_kws = {'color':'k'}
        self.label = label
        self.value = value

    def rot(self, x, y):
        return rot(x, y, self.angle)

    def trf(self, x, y):
        return trf(x, y, self.x, self.y)

    def trot(self, x, y):
        return self.trf(*self.rot(x, y))

    def ports(self):
        return (0,0)

    def __getitem__(self, key):
        ports = self.ports()

        rv = None
        if isinstance(ports, (dict, list)):
            rv = ports[key]
        elif isinstance(ports, tuple):
            assert len(ports) == 2
            rv = ports
        else:
            raise Exception(f'node port get expected dict, list or tuple, got {type(ports)}')

        assert len(rv) == 2

        return self.trot(*rv)


    def data(self):
        return [null]

    def draw(self):
        points = self.data()
        if not points:
            return
        x, y = zip(*points)
        x, y = self.rot(x, y)
        x, y = self.trf(x, y)
        plt.plot(x, y, **self.plot_kws)
        if self.label:
            self.draw_label(x, y)
        if self.value:
            self.draw_value(x, y)

    def draw_label(self, x, y):
        minx = np.nanmin(x)
        maxx = np.nanmax(x)
        midx = minx + (maxx - minx)*0.5
        maxy = np.nanmax(y)
        plt.text(midx, maxy+0.3, self.label, ha='center', va='bottom')

    def draw_value(self, x, y):
        minx = np.nanmin(x)
        maxx = np.nanmax(x)
        midx = minx + (maxx - minx)*0.5
        miny = np.nanmin(y)
        plt.text(midx, miny-0.3, self.value, ha='center', va='top')
