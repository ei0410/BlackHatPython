#!/usr/bin/env python3

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0)
y = np.arange(0)
z = np.arange(0)

for line in open("data.txt", "r"):
    value = line.split()
    x = np.append(x, float(value[0]))
    y = np.append(y, float(value[1]))
    z = np.append(z, float(value[2]))

fig = plt.figure()
ax = Axes3D(fig)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

for i in range(x.shape[0]):
    print(x[i], y[i], z[i])

max_range = np.array([x.max()-x.min(), y.max()-y.min(), z.max()-z.min()]).max() / 2.0

mid_x = (x.max()+x.min()) * 0.5 + x.min()
mid_y = (y.max()+y.min()) * 0.5 + y.min()
mid_z = (z.max()+z.min()) * 0.5 + z.min()

ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)

ax.scatter(x, y, z)
plt.show()
