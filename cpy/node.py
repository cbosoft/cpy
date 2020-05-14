import numpy as np

from cpy.util import rot, trf, null
from cpy.tikz import pic


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

    def paths(self):
        return []

    def draw(self):
        paths = self.paths()

        pic().draw_paths_transformed(paths, shift=(self.x, self.y), rotation=(self.angle))

        if self.label:
            self.draw_label()

        if self.value:
            self.draw_value()

    def draw_label(self):
        pic().draw_text(self.x, self.y, self.label, anchor='center')

    def draw_value(self):
        pic().draw_text(self.x, self.y, self.value, anchor='center')
