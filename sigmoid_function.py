import numpy
import matplotlib.pyplot


def sigmoid(x):
    return 1 / (1 + numpy.exp(-x))


if __name__ == '__main__':
    x = numpy.arange(-5.0, 5.0, 0.1)
    y = sigmoid(x)
    
    matplotlib.pyplot.plot(x, y)
    matplotlib.pyplot.ylim(-0.1, 1.1)
    matplotlib.pyplot.show()
