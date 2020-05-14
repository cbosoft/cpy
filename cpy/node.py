from matplotlib import pyplot as plt

from cpy.util import rot, trf, null


class Node:

    def __init__(self, x, y, rotation=0, label=None, value=None):
        self.x = x
        self.y = y
        self.angle = rotation
        self.plot_kws = {'color':'k'}
        self.label = label
        self.value = value

    def rot(self, x, y):
        return rot(x, y, self.angle)

    def trf(self, x, y):
        return trf(x, y, self.x, self.y)

    def centre(self):
        return self.x, self.y

    def data(self):
        return [null]

    def draw(self):
        x, y = self.data()
        plt.plot(*rot(x, y, self.angle), **self.plot_kws)
        if self.label:
            self.draw_label(x, y)
        if self.value:
            self.draw_value(x, y)

    def draw_label(self, x, y):
        minx = np.nanmin(x)
        maxx = np.nanmax(x)
        midx = minx + (maxx - minx)*0.5
        maxy = np.nanmax(y)
        plt.text(midx, maxy+0.3, self.label, ha='center', va='bottom')

    def draw_value(self, x, y):
        minx = np.nanmin(x)
        maxx = np.nanmax(x)
        midx = minx + (maxx - minx)*0.5
        miny = np.nanmin(y)
        plt.text(midx, miny-0.3, self.value, ha='center', va='top')
