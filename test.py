from cpy import *
from cpy.util import arc, hop


if __name__ == "__main__":


    with Diagram('plot.pdf') as d:
        led1 = d.add(LED(0, 0, -90))
        led2 = d.add(LED(5, 0))
        d.connect(led1['anode'], led2['cathode'], connection_type='-|')

        mc = d.add(DIPn(0, 5, n=8, label='MCP3208'))

        d.connect(led1['cathode'], mc[0], connection_type='-|')

        photo = d.add(PhotoTransistor(10, 3, label='photo1', value='$\\beta 100$'))
        pnp = d.add(TransistorPNP(15, 3, label='pnp1', value='$\\beta 400$'))
        npn = d.add(TransistorNPN(20, 3))


        n1 = d.add(Node(20, 6))
        d.connect(n1[0], npn['collector'], connection_type='-|')
        d.connect(n1[0], pnp['collector'], connection_type='-|')
        d.connect(n1[0], photo['collector'], connection_type='-|')

        n2 = d.add(Node(20, 8))
        d.connect(photo.emitter(), *hop([13,6], backwards=True), n2[0], connection_type='-|')

        res = d.add(Resistor(10, -5, value='$20\\rm\\,\\Omega$'))
        cap = d.add(Capacitor(0, -5, value='$20\\rm\\,F$', label='C1'))

        g = d.add(Ground(-5, -10))

        s = d.add(Source(0, -10, value='$5\\rm\\,V$'))





