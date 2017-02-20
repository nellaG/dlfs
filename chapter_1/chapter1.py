# vim: fileencoding=utf-8 tabstop=2 softtabstop=2 shiftwidth=2 expandtab

import sys

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.image import imread


def simple_plot():
  '''
  1.6.1 simple plot
  '''
  x = np.arange(0, 6, 0.1)
  y = np.sin(x)

  plt.plot(x, y)
  plt.show()


def sin_cos_plot():
  '''
  1.6.2 sin_cos_plot
  '''
  x = np.arange(0, 6, 0.1)
  y1 = np.sin(x)
  y2 = np.cos(x)

  plt.plot(x, y1, label="sin", color="#ffbcc3")
  plt.plot(x, y2, linestyle="--", label="cos", color="#7cf6e7")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.title("sin & cos")
  plt.legend()
  plt.show()


def load_image():
  '''
  1.6.3 load_image
  '''
  img = imread('./hdd.png')  # supports png only.
  plt.imshow(img)
  plt.show()


def main(argv):
  func = {
      '1.6.1': simple_plot,
      '1.6.2': sin_cos_plot,
      '1.6.3': load_image,
  }.get(argv)
  if func:
    print("Drawing the graph in section {} ...".format(argv))
    func()
  else:
    print("No implementaion")


if __name__ == "__main__":
  main(sys.argv[1])
