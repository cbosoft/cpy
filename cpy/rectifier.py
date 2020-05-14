from cpy.node import Node
from cpy.util import trf, rot, null

class Diode(Node):

    def ports(self):
        return {
                'anode': (1.5, 0),
                'cathode': (-1.5, 0)
            }

    def data(self):
        return [
                null,
                (-1,1),
                (-1,-1),
                null,
                (-1,0),
                (1,1),
                (1,-1),
                (-1,0),
                null,
                (1, 0),
                (1.5,0),
                null,
                (-1.0,0),
                (-1.5,0),
                null
            ]

