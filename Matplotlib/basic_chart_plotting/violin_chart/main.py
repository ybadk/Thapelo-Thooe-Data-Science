
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = [np.random.normal(0, std, 100) for std in range(1, 4)]

plt.figure()

plt.violinplot(data, showmeans=True, showmedians=True)

plt.title('Violin Plot')
plt.xlabel('Data Sets')
plt.ylabel('Values')
plt.xticks([1, 2, 3], ['Set', 'Set 2', 'Set 3'])

plt.show()
