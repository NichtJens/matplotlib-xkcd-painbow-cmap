#!/usr/bin/env python

import numpy as np
from matplotlib import pyplot as plt
from painbow import cmap


data = np.load("data.npy")

plt.xkcd()

plt.imshow(data, cmap=cmap, origin="lower")

plt.xlabel("$\\theta$ (PHASE)")
plt.ylabel("$\\lambda$", rotation=0)

cb = plt.colorbar()
cb.ax.set_ylabel("PEAK ENERGY")

ax = plt.gca()
ax.axes.xaxis.set_ticklabels([])
ax.axes.yaxis.set_ticklabels([])

plt.show()



