
import matplotlib.pyplot as plt

fig, ax = plt.subplots(2)

#row = 0, column = 2

#create data
x = [4, 5, 15, 25]

y = [10, 15, 10, 25]


ax[0].plot(x,y)
ax[1].bar(x,y)

plt.show()
