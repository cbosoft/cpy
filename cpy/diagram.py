import numpy as np

from cpy.tikz import pic
from cpy.node import Node

class Diagram:

    def __init__(self, name):
        self.paths = list()
        self.nodes = list()
        self.pic = pic(name)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.draw()
        self.pic.save()

    def connect(self, *points, connection_type='-'):

        points = [point[0] if isinstance(point, Node) else point for point in points]

        pts = list()
        for i, (point, next_point) in enumerate(zip(points, points[1:])):
            if isinstance(point, str):
                connection_type = point
                continue

            if isinstance(next_point, str):
                connection_type = next_point
            
            j = i+1
            while isinstance(next_point, str):
                j += 1
                next_point = points[j]

            pts.append(point)
            if connection_type == '-|':
                pts.append([next_point[0], point[1]])
            elif connection_type == '|-':
                pts.append([point[0], next_point[1]])
        pts.append(points[-1])
        self.pic.draw_points(pts)

    def add(self, node):
        self.nodes.append(node)
        return node

    def draw(self):
        for node in self.nodes:
            node.draw()
