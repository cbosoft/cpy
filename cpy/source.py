from cpy.node import Node

class Source(Node):

    def paths(self):
        return ['\\draw (0,0) circle (0.5);',
                '\\draw (0.5,0) -- (2.0, 0.0);']

    def ports(self):
        return (2.0, 0.0)
