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


def main(argv):
    if argv == 'and':
        for x, y in itertools.product([0, 1], [0, 1]):
            print("AND({}, {}) = {}".format(x, y, _and(x, y)))
    else:
        print("No Implementation")


if __name__ == "__main__":
    main(sys.argv[1])
