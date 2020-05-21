from cpy.node import Node
from cpy.tikz import pic


class Resistor(Node):

    def __init__(self, *args, south_label=False, **kwargs):
        super().__init__(*args, **kwargs)

        self.south_label = south_label

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
        pic().draw_text(self.x, self.y, self.value, anchor='center', rotation=self.angle)

    def draw_label(self):

        if self.south_label:
            px, py = self.trot(0, -0.6)
            a = 'north'
        else:
            px, py = self.trot(0, 0.6)
            a = 'south'
        pic().draw_text(px, py, self.label, anchor=a, rotation=self.angle)


class Capacitor(Node):

    def paths(self):
        return [
                '\\draw[thick] (-0.33,1) -- (-0.33,-1);',
                '\\draw[thick] (0.33,1) -- (0.33,-1);',
                '\\draw (-1,0) -- (-0.33,0);',
                '\\draw (1,0) -- (0.33,0);'
            ]

    def ports(self):
        return {
                'left': (-1,0), 'right': (1,0)
            }

    def draw_value(self):
        px, py = self.trot(0, -1)
        pic().draw_text(px, py, self.value, anchor='north', rotation=self.angle)

    def draw_label(self):
        px, py = self.trot(0, 1)
        pic().draw_text(px, py, self.label, anchor='south', rotation=self.angle)
