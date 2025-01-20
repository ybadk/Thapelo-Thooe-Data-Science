
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


x = [2850] 
y = [2850]

data = [np.random.normal(x, std, y) for std in range(1, 11)]
plt.figure()
plt.boxplot(data, vert=True, patch_artist=True)
plt.title('GOLD PRICE FORECAST FOR NEXT 10 YEARS')
plt.xlabel('Y10 XAU/USD')
plt.ylabel('PRICE')
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ['2026', '2027', '2028', '2029', '2030', '2031', '2032', '2033', '2034', '2035'])
plt.grid(axis='y', color='blue')
plt.show()

