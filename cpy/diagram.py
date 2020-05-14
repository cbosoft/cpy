import numpy as np
from matplotlib import pyplot as plt


class Diagram:

    def __init__(self, name):
        self.points = list()
        self.objects = list()
        self.wire_kws = {'color':'k'}
        self.name = name

    def __enter__(self):
        plt.gca().set_aspect('equal')
        plt.rc('savefig', bbox='tight')
        plt.rc('lines', linewidth=0.5)
        plt.rc('text', usetex=True)
        plt.rc('font', family='sans-serif')
        plt.rc('text.latex', preamble='\\usepackage{sansmath}\\sansmath{}')
        plt.axis('off')
        return self

    def __exit__(self, *args):
        self.draw()
        plt.savefig(self.name)

    def connect(self, *points, connection_type='-'):
        self.points.append((np.nan, np.nan))
        #self.points.extend(points)
        for point, next_point in zip(points, points[1:]):
            self.points.append(point)
            if connection_type == '-|':
                self.points.append([next_point[0], point[1]])
            elif connection_type == '|-':
                self.points.append([point[0], next_point[1]])
        self.points.append(points[-1])
        self.points.append((np.nan, np.nan))

    def add(self, o):
        self.objects.append(o)
        return o

    def draw(self):

        if self.points:
            x, y = zip(*self.points)
            plt.plot(x, y, **self.wire_kws)

        for o in self.objects:
            o.draw()
