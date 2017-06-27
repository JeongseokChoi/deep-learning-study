import numpy
import matplotlib.pyplot
from activ_func import *


X = numpy.array([1.0, 0.5])
W1 = numpy.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = numpy.array([0.1, 0.2, 0.3])
print(X.shape)
print(W1.shape)
print(B1.shape)

A1 = numpy.dot(X, W1) + B1
Z1 = sigmoid(A1)
print(A1)
print(Z1)


W2 = numpy.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2 = numpy.array([0.1, 0.2])
print(Z1.shape)
print(W2.shape)
print(B2.shape)

A2 = numpy.dot(Z1, W2) + B2
Z2 = sigmoid(A2)
print(A2)
print(Z2)


W3 = numpy.array([[0.1, 0.3], [0.2, 0.4]])
B3 = numpy.array([0.1, 0.2])

A3 = numpy.dot(Z2, W3) + B3
Y = identify(A3)
print()
print(Y)