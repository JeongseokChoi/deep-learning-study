import numpy
import matplotlib.pyplot


def relu(x):
    return numpy.maximum(0, x)


if __name__ == '__main__':
    x = numpy.arange(-5.0, 5.0, 0.1)
    y = relu(x)
    
    matplotlib.pyplot.plot(x, y)
    matplotlib.pyplot.show()
