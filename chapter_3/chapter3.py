# -*- coding: utf-8 -*-

import sys

import numpy as np
from matplotlib import pylab as plt


def step_function(x):
    return np.array(x > 0, dtype=np.int)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def relu(x):
    return np.maximum(0, x)


def main(argv):
    x = np.arange(-5.0, 5.0, 0.1)
    if argv == "step_function":
        y = step_function(x)
    elif argv == "sigmoid":
        y = sigmoid(x)
    elif argv == "relu":
        y = relu(x)
    else:
        print("no result")
        return
    plt.plot(x, y, label=argv, color="#ffbcc3")
    plt.ylim(-0.1, 1.1)
    plt.show()


if __name__ == "__main__":
    main(sys.argv[1])
