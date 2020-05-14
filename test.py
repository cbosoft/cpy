from cpy import *
from cpy.util import arc, hop
from cpy.tikz import pic


if __name__ == "__main__":

    with Diagram('plot.pdf') as d:

        pv = d.add(Source(0, 0, value='$6\\rm\\,V$'))
        g = d.add(Ground(2, -15))


        r1 = d.add(
                Resistor(2, -5,
                    rotation=-90,
                    label='R1',
                    value='$10\\rm\\,k\\Omega$'))
        n1 = d.add(Node(2, -7.5))
        r2 = d.add(Resistor(2, -10, rotation=-90, value='$10\\rm\\,k\\Omega$'))
        n2 = d.add(Node(2, -12.5))

        t = d.add(TransistorNPN(8, -7.5))

        m = d.add(Motor(9, -3, rotation=-90))

        d.connect(pv[0], r1['left'], connection_type='-|')
        d.connect(r1['right'], n1[0], r2['left'] )
        d.connect(t['base'], n1[0] )
        d.connect(pv[0], m['left'], connection_type='-|')
        d.connect(m['right'], t['collector'])
        d.connect(t['emitter'], n2[0], connection_type='|-')
        d.connect(r2['right'], n2[0], g[0])
