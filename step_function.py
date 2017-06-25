import numpy
import matplotlib.pyplot


def step_function(x):
    return numpy.array(x > 0, dtype=numpy.int)


if __name__ == '__main__':
    x = numpy.arange(-5.0, 5.0, 0.1)
    y = step_function(x)
    matplotlib.pyplot.plot(x, y)
    matplotlib.pyplot.ylim(-0.1, 1.1)
    matplotlib.pyplot.show()
