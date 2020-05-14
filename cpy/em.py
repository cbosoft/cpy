import numpy as np
from matplotlib import pyplot as plt

from cpy.node import Node
from cpy.util import circle, null

class Motor(Node):

    def data(self):

        r = 1
        pts = circle( (0, 0), 1)

        h = 0.3
        w = np.sqrt(np.subtract(r*r, h*h))
        e = 0.3

        pts.extend( [null, ( w,h), ( w+e,h), ( w+e,-h), ( w,-h), null] )
        pts.extend( [null, (-w,h), (-w-e,h), (-w-e,-h), (-w,-h), null] )

        pts.extend( [(-w-e,0), (-1.5,0),null,(w+e,0), (1.5,0)] )
    
        return pts

    def ports(self):
        return {
                'left':(-1.5,0),
                'right':(1.5,0)
            }


    def draw(self):
        super().draw()
        plt.text(self.x, self.y, "M", va='center', ha='center')

