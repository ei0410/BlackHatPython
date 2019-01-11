#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

x = 0
for line in open("data.txt", "r"):
    x = x + 1
    y = line.split()
    plt.plot(x, float(y[0]), "ro")
    plt.plot(x, float(y[1]), "go")
    plt.plot(x, float(y[2]), "bo")
    print (y[0], y[1], y[2])
plt.show()
