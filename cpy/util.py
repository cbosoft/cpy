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

def angle_between(p1, p2):

    theta = np.arccos(np.dot(p1, p2))*180.0/np.pi
    return theta


def arrow(start, length=None, end=None, rotation=0, inline=False, backwards=False):

    if length is None and end is None:
        raise Exception("arrow needs either a length or an end")

    if end is not None:
        l = np.sqrt(np.sum(np.power(np.subtract(start, end), 2.0)))
        r = angle_between(start, end)-90
        dx, dy = np.subtract(end, start)

        if dx < 0 and dy < 0:
            r -= 180
        elif dy < 0 or dy < 0:
            r -= 90

        return arrow(start, length=l, rotation=r, inline=inline, backwards=backwards)

    l = length

    al = 0.3*l
    aw = 0.15

    pts = [
            (0, 0),
            (0, l),
            (-aw, l-al),
            null,
            (0, l),
            (aw, l-al),
            null
        ]

    if not inline:
        pts.insert(0, null)
    else:
        pts.append( (0, l) )

    x, y = zip(*pts)

    if backwards:
        y = np.add(l, np.multiply(y, -1))

    x, y = rot(x, y, rotation)
    x, y = trf(x, y, *start)
    return list(zip(x, y))


    if horizontal:

    if backwards:


def arrowhead(centre, rotation=0, tail=None):
    x, y = centre
    paths = [
            '\\begin{scope}[shift={' + f'({x},{y})' + '}, rotate=' + f'{rotation}' + ']',
            '\\filldraw (0,0) -- (0.15,-0.5) -- (-0.15,-0.5) -- cycle;'
            '\\end{scope}'
        ]
    if tail:
        paths.insert(1, f'\\draw (0,0) -- (0,{-float(tail)});')
    return ''.join(paths)
