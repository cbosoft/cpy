from cpy.node import Node
from cpy.util import trf, rot, null
from cpy.tikz import pic

class Diode(Node):

    def ports(self):
        return {
                'anode': (1.5, 0),
                'cathode': (-1.5, 0)
            }

    def paths(self):
        return [
                '\\draw (-1,1) -- (-1,-1);',
                '\\draw (-1,0) -- (1,1) -- (1,-1) -- cycle;',
                '\\draw (1,0) -- (1.5,0);'
                '\\draw (-1,0) -- (-1.5,0);'
            ]

    def draw_label(self):
        angle = int(self.angle) % 180
        px, py = rot(0, 2.0*abs(self.scale[1]), angle)
        pic().draw_text(*self.trf(px, py), self.label, rotation=angle)
