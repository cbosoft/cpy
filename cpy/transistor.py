import numpy as np

from cpy.util import trf, null, arrowhead, angle_between
from cpy.node import Node
from cpy.tikz import pic

class _TransistorCommon(Node):

    def paths(self):
        return [
                '\\draw (1,2) -- (1,1.5) -- (0,0.6);',
                '\\draw (1,-2) -- (1,-1.5) -- (0,-0.6);',
                '\\draw[ultra thick] (0,1.2) -- (0,-1.2);',
            ]

    def draw_label(self):
        if self.value:
            x, y = self.trot(0.5, 0.4)
        else:
            x, y = self.trot(0.5, 0.0)

        angle = int(self.angle) % 180
        if angle > 0:
            a = 'center'
        else:
            a = 'west'
        pic().draw_text(x, y, self.label, anchor=a)

    def draw_value(self):
        if self.label:
            x, y = self.trot(0.5, -0.4)
        else:
            x, y = self.trot(0.5, 0.0)
        angle = int(self.angle) % 180
        if angle > 0:
            a = 'center'
        else:
            a = 'west'
        pic().draw_text(x, y, self.value, anchor=a)

    def ports(self):
        return {
                'collector': (1,2),
                'emitter': (1,-2)
            }

class TransistorNPN(_TransistorCommon):

    def paths(self):
        paths = super().paths()
        paths.append('\\draw (0,0) -- (-0.5,0);')
        paths.append(arrowhead([1, -1.5], 225 ))
        return paths

    def ports(self):
        return {
                'base': (-0.5, 0),
                'collector': (1,2),
                'emitter': (1,-2)
            }


class TransistorPNP(_TransistorCommon):

    def paths(self):
        paths = super().paths()
        paths.append('\\draw (0,0) -- (-0.5,0);')
        paths.append(arrowhead([1, 1.5], 315 ))
        return paths


class PhotoTransistor(_TransistorCommon):

    def paths(self):
        paths = super().paths()
        paths.append('\\draw (0.5,0) circle (1.7);')
        paths.append(arrowhead([-0.9, 1.5], 225, tail=1.0 ))
        paths.append(arrowhead([-1.2, 1.2], 225, tail=1.0 ))
        paths.append(arrowhead([1, -1.5], 225 ))
        return paths

