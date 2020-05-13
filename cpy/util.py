import numpy as np

def rot(x, y, a):
    a = np.pi*a/180.0
    xp = np.subtract(np.multiply(x, np.cos(a)), np.multiply(y, np.sin(a)))
    yp = np.add(np.multiply(y, np.cos(a)), np.multiply(x, np.sin(a)))
    return xp, yp

def trf(x, y, ox, oy):
    return np.add(x, ox), np.add(y, oy)

null = (np.nan, np.nan)
