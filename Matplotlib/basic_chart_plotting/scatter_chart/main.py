
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

y = [10, 20, 30, 40, 50, 50, 40, 30, 20, 10]


plt.figure()

plt.scatter(x,  y, color='g', marker='^')

plt.title('Random Scale out of 100')
plt.show()
