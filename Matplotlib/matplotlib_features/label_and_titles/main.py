
import matplotlib.pyplot as plt
import numpy as np


ypoints = np.array([1, 2, 5, 9, 11, 12, 13, 16, 2])

t_font = {'color' : 'blue'}
label_x = {'color' : 'red'}
label_y = {'color' : 'green'}


plt.title("Title", fontdict = t_font)
plt.xlabel("x-axis", fontdict = label_x)
plt.ylabel("y-axis", fontdict = label_y)

plt.plot(ypoints, '^')

plt.show()
