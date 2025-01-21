
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

labels = ['Boxer-Stores', 'Shoprite-Stores', 'Clicks-Stores', 'Woolworths-Stores', 'Spar-Stores']

sizes = [20, 25, 15, 25,  15]

colors = ['gold', 'lightskyblue', 'green', 'red', 'blue']

explode=(0.5, 0, 0, 0, 0)

plt.title('BIGGEST RETAIL BRANDS IN SOUTH AFRICA')


plt.pie(sizes, explode=explode, labels=labels, colors=colors)

plt.show()
