import numpy as np

from cpy.util import null
from cpy.node import Node
from cpy.tikz import pic

class DIPn(Node):

    def __init__(self, x, y, n=1, w=2, named_ports=None, show_named=False, draw_semicircle=True, **kwargs):
        super().__init__(x, y, **kwargs)
        self.n = n
        self.w = w
        self.named_ports = named_ports
        self.show_named = show_named
        self.draw_semicircle = draw_semicircle

    def port(self, index):

        h = (self.n-1)/2
        yb = self.w/2
        y = yb+0.5
        x = -h+index

        if index > (self.n-1):
            i = 2*self.n - index-1
            x = -h+i
        else:
            y = -y

        return x,y


    def paths(self):

        h = (self.n-1)/2
        yb = self.w/2
        t = 0.5

        paths = [f'\\draw ({-h-t},{yb}) rectangle ({h+t},{-yb});']

        for i in range(self.n):
            paths.append(f'\\draw ({-h+i}, {yb}) -- ++ (0, 0.5);')
            paths.append(f'\\draw ({-h+i},{-yb}) -- ++ (0,-0.5);')

        if self.draw_semicircle:
            paths.append(f'\\draw ({-h-t},0.2) arc(90:-90:0.2);')
        return paths

    def ports(self):
        numbered = {i:self.port(i) for i in range(2*self.n)}
        named = self.named_ports if self.named_ports else dict()

        named = dict()
        if self.named_ports:
            for (name, port) in self.named_ports.items():
                named[name] = numbered[port]

        return {**numbered, **named}

    def draw_label(self):
        if self.show_named:
            for name, i in self.named_ports.items():
                px, py = self.port(i)
                if py > 0:
                    py -= 0.7
                    a = 'east'
                else:
                    py += 0.7
                    a = 'west'
                x, y = self.trot(px, py)
                pic().draw_text(x, y, name, anchor=a, rotation=self.angle+90)

        pic().draw_text(self.x, self.y, self.label, anchor='center', rotation=self.angle)

    def draw_value(self):
        pass



class DIP6(DIPn):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, n=6)
