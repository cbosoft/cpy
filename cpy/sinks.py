from cpy.node import Node
from cpy.util import null

class Ground(Node):

    def data(self):

        return [
                null,
                (-1,0), (1,0),
                null,
                (-0.5,-0.5), (0.5, -0.5),
                null,
                (-0.25,-1), (0.25,-1),
                null,
                (0,0), (0,1),
                null
            ]

    def draw_value(self, *args):
        pass
