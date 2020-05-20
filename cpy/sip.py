from cpy.dip import DIPn
from cpy.util import null
from cpy.tikz import pts2path


class SIPn(DIPn):

    def port(self, index):

        h = (self.n-1)/2
        y = (self.w + 1)/-2
        x = -h+index
        return x,y


    def paths(self):

        h = (self.n-1)/2
        y = (self.w)/2
        t = 0.5

        paths = list()
        paths.append(f'\\draw ({-h-t},{y}) rectangle  ({h+t},{-y});')

        for i in range(self.n):
            paths.append(f'\\draw ({-h+i},{-y}) -- ++(0,-0.5);')

        if self.draw_semicircle:
            paths.append(f'\\draw ({-h-t},0.2) arc(90:-90:0.2);')
        return paths
