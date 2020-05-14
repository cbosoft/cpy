import numpy as np

def rot(x, y, a):

    if isinstance(a, tuple):
        rx, ry = a[1:]
        a = a[0]
    else:
        rx, ry = 0, 0
    
    a = np.pi*a/180.0

    x = np.add(x, rx)
    y = np.add(y, ry)
    xp = np.subtract(np.multiply(x, np.cos(a)), np.multiply(y, np.sin(a)))
    yp = np.add(np.multiply(y, np.cos(a)), np.multiply(x, np.sin(a)))
    xp = np.subtract(xp, rx)
    yp = np.subtract(yp, ry)
    return xp, yp

def trf(x, y, ox, oy):
    return np.add(x, ox), np.add(y, oy)

null = (np.nan, np.nan)
