from cpy.node import Node
from cpy.tikz import pic

class Source(Node):

    def paths(self):
        return ['\\draw (0,0) circle (0.5);',
                '\\draw (0.5,0) -- (2.0, 0.0);']

    def ports(self):
        return (2.0, 0.0)

    def draw_label(self):
        x, y = self.trot(0, 0.75)
        pic().draw_text(x, y, self.label, anchor='center', rotation=self.angle)

    def draw_value(self):
        x, y = self.trot(0, -0.75)
        pic().draw_text(x, y, self.value, anchor='center', rotation=self.angle)
