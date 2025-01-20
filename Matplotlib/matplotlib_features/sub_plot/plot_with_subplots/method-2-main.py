
import matplotlib.pyplot as plt

#create data
x = [1, 2, 2, 3, 4, 5 ]
y = [2, 4, 6, 8, 10, 12]

fig, (ax1, ax2) = plt.subplots(1,2)

ax1.plot(x,y)
ax2.bar(x,y)

fig.suptitle('fig, ax1, ax2')

plt.show()
