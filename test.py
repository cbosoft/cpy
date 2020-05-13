from cpy.diagram import Diagram
from cpy.light import LED
from cpy.dip import DIP6


if __name__ == "__main__":

    with Diagram('plot.pdf') as d:
        led1 = d.add(LED(0, 0))
        led2 = d.add(LED(5, 0))
        d.connect(led1.anode(), led2.cathode())

        mc = d.add(DIP6(0,5))

        d.connect(led1.cathode(), mc.port(0), connection_type='-|')


