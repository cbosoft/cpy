import numpy as np

import os

def pts2path(points, opts=''):
    s = '\\draw '

    if opts:
        s += f'[{opts}] '
    
    continuing = False
    for point in points:
        if np.any(np.isnan(point)):
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
            r'\begin{tikzpicture}',
            r'\usetikzlibrary{decorations.pathreplacing}'
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
        os.system(f'mv {path}.pdf {self.name}')
        os.system(f'rm {path}*')

    def draw_points(self, points):
        self.paths.append(pts2path(points))

    def draw_paths(self, paths):
        for path in paths:
            self.paths.append(path)

    def draw_paths_transformed(self, paths, shift=(0,0), rotation=0, scale=(1.0,1.0)):
        assert isinstance(shift, tuple) and len(shift) == 2
        sh_x, sh_y = shift

        assert isinstance(scale, tuple) and len(scale) == 2
        sc_x, sc_y = scale

        self.paths.append(r'\begin{scope}[shift={'+f'({sh_x},{sh_y})'+'}, rotate=' + f'{rotation}, xscale={sc_x}, yscale={sc_y}]')
        self.draw_paths(paths)
        self.paths.append(r'\end{scope}')

    def draw_text(self, x, y, t, rotation=0, anchor='center', colour='black', default_size='LARGE', **kwargs):
        self.paths.append(f'\\node [rotate={rotation},anchor={anchor},{colour}] (n) at ({x},{y}) {{\\{default_size} {t}}};')



t = None

def pic(name=None):
    global t
    if not t:
        t = TikzPicture(name)
    return t
