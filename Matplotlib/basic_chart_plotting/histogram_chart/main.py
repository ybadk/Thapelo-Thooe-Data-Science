
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = ([2025, 2026, 2027, 2027, 2029, 2030, 2031, 2032, 2033, 2034, 2035])
y = np.arange(800000, 1000000)
plt.figure()
color = ['yellow']

plt.hist(data, bins=5, color=color, edgecolor='blue')

plt.show()
