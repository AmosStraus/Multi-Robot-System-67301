import numpy as np


def read_pgm(pgmf):
    """Return a net of integers from a PGM as a list of lists."""

    # FIRST TWO LINES ARE GARBAGE
    pgmf.readline()
    pgmf.readline()
    width, height = [int(i) for i in pgmf.readline().split()]
    depth = int(pgmf.readline())
    assert depth <= 255

    net = []
    for y in range(height):
        row = []
        for y in range(width):
            row.append(ord(pgmf.read(1)))
        net.append(row)
    return np.array(net)


f = open('D:\\2021b_HUJI\\MultiRobotSystems\\map1.pgm')
r = read_pgm(f)
