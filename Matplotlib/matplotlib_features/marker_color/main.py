
import matplotlib.pyplot as plt
import numpy as np


ypoints = np.array([2, 5, 6, 11, 2, 6, 10, 5, 0])

plt.figure()
plt.grid(color='blue')
plt.plot(ypoints, marker = 'o', ms = '20', mec = 'b', mfc = 'y')


plt.show()
