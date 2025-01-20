
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([10, 20, 5, 15, 6, 8, 4, 12, 8, 3])

plt.figure()
plt.grid(color='b')
plt.plot(ypoints, '^-b', ms = 30, mec = 'r', mfc = 'g')

plt.show()
