
import matplotlib.pyplot as plt
import numpy as np

#-------------------- MARKER ----------------------------#

#Marker - mark the data points on a line plot


#Styles available : 'o', 's', 'D', 'd', 'x', 'X', 'P', 'p', 'H', 'h', 'v'
# 'v', '1', '2', '3','4' '^', '<', '>' ','

ypoints = np.array([1, 3, 14, 6, 9, 11, 8, 5, 2, 0, 7])

plt.figure()

plt.grid(color='blue')

plt.plot(ypoints, c = 'b', marker = '^', ms=30)

plt.show()
