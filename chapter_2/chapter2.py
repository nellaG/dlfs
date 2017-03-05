# -*- coding: utf-8 -*-

import itertools
import sys

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.image import imread


def _and(x1: int, x2: int) -> int:
    '''
    create AND gate using the perceptron.
    '''
    w1 = 0.5
    w2 = 0.5
    theta = 0.7

    tmp = x1 * w1 + x2 * w2

    return int(tmp > theta)


def _and_improved(x1: int, x2: int) -> int:
    '''
    create AND gate with bias and weight.
    '''
    x = np.array([x1, x2])
    weight = np.array([0.5, 0.5])
    # -theta goes to bias
    bias = -0.7

    tmp = np.sum(weight * x) + bias

    return int(tmp > 0)


def nand(x1: int, x2: int) -> int:
    '''
    create NAND gate using the perceptron.
    '''
    x = np.array([x1, x2])
    weight = np.array([0.5, 0.5])
    # -theta goes to bias
    bias = 0.7

    tmp = np.sum(weight * x) + bias

    return int(tmp > 0)


def _or(x1: int, x2: int) -> int:
    '''
    create NAND gate using the perceptron.
    '''
    x = np.array([x1, x2])
    weight = np.array([0.5, 0.5])  # only the weight and the bias are different compare to AND gate.  # noqa
    # -theta goes to bias
    bias = -0.2

    tmp = np.sum(weight * x) + bias

    return int(tmp > 0)


def main():
    for x, y in itertools.product([0, 1], [0, 1]):
        print("AND({}, {}) = {}".format(x, y, _and(x, y)))

    for x, y in itertools.product([0, 1], [0, 1]):
        print("AND_IMPROVED({}, {}) = {}".format(x, y, _and_improved(x, y)))

    for x, y in itertools.product([0, 1], [0, 1]):
        print("NAND({}, {}) = {}".format(x, y, nand(x, y)))

    for x, y in itertools.product([0, 1], [0, 1]):
        print("OR({}, {}) = {}".format(x, y, _or(x, y)))


if __name__ == "__main__":
    main()
