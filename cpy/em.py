import numpy as np

from cpy.node import Node
from cpy.util import null
from cpy.tikz import pts2path

class Motor(Node):

    def paths(self):
        pts = [
                '\\draw[thick] (0,0) circle (1);',
                '\\node (motor) at (0,0) {\\huge M};'
            ]
        r = 1

        h = 0.3
        w = np.sqrt(np.subtract(r*r, h*h))
        e = 0.3
        pts.append(pts2path([null, ( w,h), ( w+e,h), ( w+e,-h), ( w,-h), null]))
        pts.append(pts2path([null, (-w,h), (-w-e,h), (-w-e,-h), (-w,-h), null]))
        pts.append(pts2path([(-w-e,0), (-1.5,0),null,(w+e,0), (1.5,0)]))
        return pts

    def ports(self):
        return {
                'left':(-1.5,0),
                'right':(1.5,0)
            }
