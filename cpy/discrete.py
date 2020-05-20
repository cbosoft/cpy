from cpy.node import Node
from cpy.tikz import pic


class Resistor(Node):

    def paths(self):
        return [
                '\\draw (-1.5,0.5) rectangle (1.5,-0.5);',
                '\\draw (-2,0) -- (-1.5,0);'
                '\\draw (2,0) -- (1.5,0);'
            ]

    def ports(self):
        return {
                'left': (-2,0), 'right': (2,0)
            }

    def draw_value(self):
        py = 0
        if self.label:
            py -= 0.25
        px, py = self.trot(0, py)
        pic().draw_text(px, py, self.value, anchor='center', rotation=self.angle)

    def draw_label(self):
        py = 0
        if self.label:
            py += 0.25
        px, py = self.trot(0, py)
        pic().draw_text(px, py, self.label, anchor='center', rotation=self.angle)


class Capacitor(Node):

    def paths(self):
        return [
                '\\draw (-0.5,1) -- (-0.5,-1);',
                '\\draw (0.5,1) -- (0.5,-1);',
                '\\draw (-1,0) -- (-0.5,0);',
                '\\draw (1,0) -- (0.5,0);'
            ]

    def ports(self):
        return {
                'left': (-1,0), 'right': (1,0)
            }

    def draw_value(self):
        pic().draw_text(self.x-1.5, self.y, self.value, anchor='center')
