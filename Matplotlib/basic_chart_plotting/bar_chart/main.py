
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

strikers = ['Messi', 'C.Ronaldo', 'Salah', 'Rodrygo', 'Yamal', 'Gueller']

goals = [31, 33, 30, 25, 25, 26]

plt.figure()
plt.bar(strikers, goals)
plt.xlabel('Best Strikers in Football 2025')
plt.ylabel('Goals')
plt.title('2025 BEST STRIKERS IN FOOTBALL')
plt.show()
