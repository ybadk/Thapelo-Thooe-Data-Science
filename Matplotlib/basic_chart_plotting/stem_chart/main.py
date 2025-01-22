
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0.1, 2 * np.pi, 50)

y = np.cos(x)

plt.figure()

plt.stem(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Stem Plot')
plt.show()
