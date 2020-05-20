import numpy as np

from cpy.util import rot, trf, null
from cpy.tikz import pic


class Node:

    def __init__(self, x, y, rotation=0, label=None, value=None, scale=1.0, xscale=None, yscale=None, flipx=False, flipy=False, draw=None):
        self.x = x
        self.y = y
        self.angle = rotation
        self.plot_kws = {'color':'k'}
        self.label = label
        self.value = value

        sc_x = scale
        sc_y = scale

        if xscale or yscale:
            sc_x = xscale if xscale else 1.0
            sc_y = yscale if yscale else 1.0

        if flipx:
            sc_x = -abs(sc_x)
        if flipy:
            sc_y = -abs(sc_y)

        self.scale = (sc_x, sc_y)
        if not draw:
            draw = list()
        elif isinstance(draw, str):
            draw = [draw]
        self.paths_override = draw



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

        rv = np.multiply(self.scale, rv)

        return self.trot(*rv)

    def paths(self):
        return self.paths_override

    def draw(self):
        paths = self.paths()

        pic().draw_paths_transformed(paths, shift=(self.x, self.y), rotation=(self.angle), scale=self.scale)

        if self.label:
            self.draw_label()

        if self.value:
            self.draw_value()

    def draw_label(self):
        x, y = self.trot(0, 0.5)
        pic().draw_text(x, y, self.label, anchor='center', rotation=self.angle)

    def draw_value(self):
        x, y = self.trot(0, -0.5)
        pic().draw_text(x, y, self.value, anchor='center', rotation=self.angle)
