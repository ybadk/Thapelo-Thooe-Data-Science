
import matplotlib.pyplot as plt 
import numpy as np

#Multiple lines - plot x and y axis seperately

x = np.array([1, 100, 25 , 50, 35, 70, 10, 5, 0])

y = np.array([1, 100, 60, 45, 37, 80, 25, 4, 10])

z = np.array([1, 20, 36, 25, 85, 57, 69, 95, 85])
plt.plot(x, marker ='^')
plt.plot(y, marker = '>')
plt.plot(z, 'o:b')
plt.show()
