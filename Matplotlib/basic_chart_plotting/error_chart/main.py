
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0, 10, 1)
y = np.sin(x)

yerr = 0.2


plt.figure()

plt.errorbar(x, y, yerr=yerr, fmt='o', color='blue', ecolor='red')


plt.xlabel('X')
plt.ylabel('Y')
plt.title('Error Bar plot')

plt.show()
