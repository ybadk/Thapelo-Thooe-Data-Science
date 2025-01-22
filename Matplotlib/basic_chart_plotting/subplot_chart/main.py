
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


x = [2025, 2026, 2027, 2028, 2029]
y1 = [3, 6, 19, 12, 5]
y2 = [2, 4, 16, 8, 1]





plt.figure(figsize=(10, 10))

#plot 1
plt.subplot(2, 2, 1)

plt.plot(x, y1, color='green', marker='^')
plt.grid(color='red')
plt.title('Gauteng - Special Economic Zones')


#plot 2
plt.subplot(2, 2, 2)
plt.plot(x, y1, color='orange', marker='o')
plt.grid(axis='y', color='green')
plt.title('North West - Special Economic Zones')


#plot 3
plt.subplot(2, 2, 3)
plt.plot(x, y2, color='blue', marker='o')
plt.grid(color='blue')
plt.xlabel('Eastern Cape - Special Economic Zones')


#Plot 4
plt.subplot(2, 2, 4)
plt.plot(x, y1, color='red', marker='^')
plt.xlabel('Western Cape - Special Economic Zones')

plt.grid(color='red', axis='x')





plt.show()
