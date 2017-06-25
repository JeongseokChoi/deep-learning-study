import numpy


def AND(x1, x2):

    x = numpy.array([x1, x2])
    w = numpy.array([0.5, 0.5])
    b = -0.75
    
    tmp = numpy.sum(x * w) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def NAND(x1, x2):

    x = numpy.array([x1, x2])
    w = numpy.array([-0.5, -0.5])
    b = 0.75
    
    tmp = numpy.sum(x * w) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def OR(x1, x2):

    x = numpy.array([x1, x2])
    w = numpy.array([0.5, 0.5])
    b = -0.25
    
    tmp = numpy.sum(x * w) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def XOR(x1, x2):

    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

