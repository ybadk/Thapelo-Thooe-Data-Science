
#font of title and labels
# use case for fontdict parameter



import matplotlib.pyplot as plt
import numpy as np


font1 = {
        'family' : 'serif',
        'color' : 'blue', 'size' : 45


        }

font2 = {
        'font' : 'serif',
        'color' : 'green', 'size' : 25


        }

# 'loc' to position the title
plt.title("Title", fontdict = font1, loc = 'right')
plt.xlabel("x-axis", fontdict = font2)
plt.ylabel("y - axis", fontdict = font2)





#grid lines example
plt.grid()
plt.show()


