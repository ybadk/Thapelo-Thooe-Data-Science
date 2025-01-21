
import pandas as  pd
import numpy as np
import matplotlib.pyplot as plt


X, Y = np.meshgrid(np.arange(-2, 2, 0.2), np.arange(-2, 2, 0.2))

U = -1 - X**2 + Y
V = 1 + X - Y**2

plt.figure()
plt.quiver(X, Y, U, V)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Quiver Plot')
plt.show()

