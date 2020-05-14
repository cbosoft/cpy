import numpy as np

import os

def pts2path(points, opts=''):
    s = '\\draw '

    if opts:
        s += f'[{opts}] '
    
    continuing = False
    for point in points:
        if np.isnan(point[0]):
            continuing = False
            continue

        x, y = point

        if continuing:
            s += f'-- ({x},{y})'
        else:
            s += f'({x},{y})'
            continuing = True
    s += ';'
    return s



class TikzPicture:

    tex_head = [
            r'\documentclass[tikz, border=10pt]{standalone}',
            r'\usepackage{tikz}',
            r'\renewcommand\familydefault\sfdefault',
            r'\usepackage{sansmath}\sansmath{}',
            r'\begin{document}',
            r'\begin{tikzpicture}'
        ]
    tex_foot = [
            r'\end{tikzpicture}',
            r'\end{document}'
        ]

    def __init__(self, name=None):
        self.name = name
        self.paths = list()

    def write_tex(self, texfile):
        with open(texfile, 'w') as f:
            for line in self.tex_head:
                f.write(f'{line}\n')
            for path in self.paths:
                f.write(f'  {path}\n')
            for line in self.tex_foot:
                f.write(f'{line}\n')

    def save(self):
        tmp_dir = '/tmp'
        name = 'tikdia'
        path = f'{tmp_dir}/{name}'
        self.write_tex(f'{path}.tex')
        os.system(f'cd {tmp_dir} && pdflatex -interaction=nonstopmode {name}')
        os.system(f'cp {path}.pdf {self.name}')

    def draw_points(self, points):
        self.paths.append(pts2path(points))

    def draw_paths(self, paths):
        for path in paths:
            self.paths.append(path)

    def draw_paths_transformed(self, paths, shift=(0,0), rotation=0):
        assert isinstance(shift, tuple)
        sx, sy = shift
        self.paths.append(r'\begin{scope}[shift={'+f'({sx},{sy})'+'}, rotate=' + f'{rotation}' + ']')
        self.draw_paths(paths)
        self.paths.append(r'\end{scope}')

    def draw_text(self, x, y, t, **kwargs):
        self.paths.append(f'\\node (n) at ({x},{y}) {{{t}}};')



t = None

def pic(name=None):
    global t
    if not t:
        t = TikzPicture(name)
    return t
