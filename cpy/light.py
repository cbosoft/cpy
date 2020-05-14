import numpy as np

from cpy.util import trf, arrow
from cpy.rectifier import Diode

class LED(Diode):

    def data(self):
        pts = super().data()

        apts = [
                (-0.3,0.8), (-0.3,1.3),
                (np.nan, np.nan),
                (0.3,0.8), (0.3,1.3),
                (np.nan, np.nan),
                (-0.5, 1.1), (-0.3, 1.3), (-0.1, 1.1),
                (np.nan, np.nan),
                (0.5, 1.1), (0.3, 1.3), (0.1, 1.1),
            ]

        #pts.extend(apts)
        pts.extend(arrow((0.3,1.2), length=0.8, rotation=(26.7, -0.3, 0.0) ))
        pts.extend(arrow((-0.3,1.2), length=0.8, rotation=(26.7, -0.9, 0.0) ))
        return pts
