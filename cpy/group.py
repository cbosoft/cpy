from cpy.node import Node
from cpy.tikz import pic

class Group(Node):

    def __init__(self, x, y, w, h, *args, **kwargs):
        super().__init__(x, y, *args, **kwargs)
        self.w = w
        self.h = h

    def paths(self):
        return [f'\\draw[gray,thick,dashed] (0,0) rectangle ({self.w},{self.h});']

    def draw_label(self):
        pic().draw_text(self.x+0.5, self.y+0.5, self.label, anchor='south west', colour='gray', default_size='huge')


