
#Line color change
#use color or c or use  shortcut string
#-------------- WAYS TO SPECIFY COLOR --------------#
# -- NAME COLOR --- 
# red, blue, green
#---- COLOR CODES -----

#r for red, g fpr green, b for blue

import numpy as np

import matplotlib.pyplot as plt

ypoints = np.array([2, 4, 3, 6, 12, 10, 5, 2, 6, 4])

plt.figure()
plt.grid(color = 'b')
plt.plot(ypoints, 'r') #y-axis

plt.show()

