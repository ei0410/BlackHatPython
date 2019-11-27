#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

x = 0
yx = 0
yy = 0
yz = 0

for line in open("data.txt", "r"):
    x = x + 1
    y = line.split()

    yx += float(y[0])
    yy += float(y[1])
    yz += float(y[2])
    plt.plot(x, yx, "ro")
    plt.plot(x, yy, "go")
    plt.plot(x, yz, "bo")
    print (yx, yy, yz)
plt.show()
