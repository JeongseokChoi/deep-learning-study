import numpy as np


def step(x):
    return np.array(x > 0, dtype=np.int)


def relu(x):
    return np.maximum(x, 0)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def identify(x):
    return x
