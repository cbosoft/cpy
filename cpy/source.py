from cpy.util import null, circle
from cpy.node import Node

class Source(Node):

    def data(self):
        r = 0.5
        return [
                null,
                *circle( [0,0], r),
                null,
                (r,0),
                (2.0-r,0),
                null
            ]
