
# linestyle or ls froo shortcut string
#e.g '--', '-.', '.', ',', 'o', 'v', '^', '<', '>', '+', '|', '__', '*', ':'


import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([2, 6, 3, 7, 10, 8, 5, 3, 2])

plt.figure()


plt.plot(ypoints, 'v')

plt.show()
