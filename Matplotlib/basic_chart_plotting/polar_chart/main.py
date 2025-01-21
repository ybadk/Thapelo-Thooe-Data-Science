
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


theta = np.linspace(0, 2*np.pi, 100)

r = np.abs(np.sin(theta))

plt.figure()
ax = plt.subplot(111, polar=True)
ax.plot(theta, r)
ax.set_title('polar Plot')
plt.show()

