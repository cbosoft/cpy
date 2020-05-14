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
        pic().draw_text(self.x, self.y+1.5, self.label)
