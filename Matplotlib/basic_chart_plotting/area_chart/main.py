
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#call instance
x = np.linspace(0, 10, 100)

#create data
y1 = np.sin(x)
y2 = np.cos(x)

#create the area plot 
plt.fill_between(x, y1, alpha=0.5, color='yellow', label='area under sin(x)')
plt.fill_between(x, y2, alpha=0.5, color='lightgreen', label='area under sin(x)')

#show plot
plt.show()

