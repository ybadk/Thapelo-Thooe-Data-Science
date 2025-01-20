
import matplotlib.pyplot as plt

fig, ax = plt.subplots(2, 2)

x = [5, 10, 15, 20, 25]
y = [10, 15, 20, 25, 35] 

ax[0, 0].plot(x, y)
ax[0, 1].plot(x, y,  'tab:blue')
ax[1, 0].plot(x, y, 'tab:green')
ax[1, 1].plot(x, y, 'tab:red')

plt.show()
