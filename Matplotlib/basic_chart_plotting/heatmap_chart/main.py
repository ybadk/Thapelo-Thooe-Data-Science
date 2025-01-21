
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data_matrix = np.random.rand(10, 10)
plt.figure()
plt.imshow(data_matrix, cmap='viridis', interpolation='nearest')
plt.colorbar()
plt.title('Heat Map')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
