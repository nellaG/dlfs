# -*- encoding: utf-8 -*-

import typing

import numpy as np


def init_network() -> typing.Dict[str, list]:
    """
    initializes weight and bias, and saves to the variable 'network'.
    """

    network = {}
    network['W1'] = np.array([
                                 [0.1, 0.3, 0.5],
                                 [0.2, 0.4, 0.6]
                             ])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([
                                 [0.1, 0.4],
                                 [0.2, 0.5],
                                 [0.3, 0.6]
                             ])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([
                                 [0.1, 0.3],
                                 [0.2, 0.4]
                             ])
    network['b3'] = np.array([0.1, 0.2])

    return network


def sigmoid(x: int) -> float:
    return 1 / (1 + np.exp(-x))


def softmax(a: np.ndarray) -> np.ndarray:
    c = np.max(a)
    exp_a = np.exp(a - c)  # resolve overflow
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y


def forward(network: typing.Dict[str, list], x: np.ndarray) -> np.ndarray:
    """
    input -> output ("Forward")
    """
    W1 = network['W1']
    W2 = network['W2']
    W3 = network['W3']
    b1 = network['b1']
    b2 = network['b2']
    b3 = network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3

    y = a3  # identify_function(a3)
    return y


def main():
    network = init_network()
    x = np.array([1.0, 0.5])
    y = forward(network, x)
    print(y)


if __name__ == "__main__":
    main()
