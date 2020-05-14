import numpy as np

from cpy.util import trf, arrowhead
from cpy.rectifier import Diode

class LED(Diode):

    def paths(self):
        pts = super().paths()
        pts.append(arrowhead([-0.1, 1.8], tail=0.8, rotation=26.7))
        pts.append(arrowhead([-0.7, 1.6], tail=0.8, rotation=26.7))
        return pts
