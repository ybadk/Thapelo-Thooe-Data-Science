
import matplotlib.pyplot as plt

#create data
x = [0, 1, 2, 3, 4, 5]
y = [3, 6, 9, 12, 10, 13]

fig, ax = plt.subplots(1,2)

ax[0].plot(x,y)
ax[1].bar(x,y)

fig.suptitle('figure of 2 plots')
plt.show()
