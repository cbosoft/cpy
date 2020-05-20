from cpy.dip import DIPn

class Headern(DIPn):

    def port(self, index):

        h = (self.n-1)/2
        x = -h+index

        if index > (self.n-1):
            y = 1.0
            i = 2*self.n - index-1
            x = -h+i
        else:
            y = -1.0

        return x,y

    def paths(self):

        h = (self.n-1)/2
        t = 0.5

        paths = list()

        paths.append(f'\\draw ({-h-0.5},1.5) rectangle ({h+0.5},-1.5);')
        for i in range(self.n):
            for iy in [-1,1]:
                ix = i-h
                paths.append(f'\\draw ({ix},{iy}) circle (0.4);')
        return paths


class OnesideHeadern(DIPn):

    def port(self, index):

        h = (self.n-1)/2
        x = -h+index
        y = -1.0

        return x,y

    def paths(self):

        h = (self.n-1)/2
        t = 0.5

        paths = list()

        paths.append(f'\\draw ({-h-0.5},0.5) rectangle ({h+0.5},-1.5);')
        for i in range(self.n):
            ix = i-h
            paths.append(f'\\draw ({ix},-1) circle (0.4);')
        return paths
