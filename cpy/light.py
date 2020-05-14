import numpy as np

from cpy.util import trf
from cpy.rectifier import Diode

class LED(Diode):

    def __init__(self, x, y, rotation=0):
        super().__init__(x, y, rotation)

    def data(self):
        pts = [
                (-1,1), (-1,-1),
                (np.nan, np.nan),
                (-1,0), (1,1),
                (1,-1), (-1,0),
                (np.nan, np.nan),
                (1, 0),
                (np.nan, np.nan),
            ]

        apts = [
                (-0.3,0.8), (-0.3,1.3),
                (np.nan, np.nan),
                (0.3,0.8), (0.3,1.3),
                (np.nan, np.nan),
                (-0.5, 1.1), (-0.3, 1.3), (-0.1, 1.1),
                (np.nan, np.nan),
                (0.5, 1.1), (0.3, 1.3), (0.1, 1.1),
            ]
        pts.extend(apts)
        return pts
