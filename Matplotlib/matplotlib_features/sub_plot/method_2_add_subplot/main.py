
import matplotlib.pyplot as plt

#method 2 - add sub_plot

#Syntax:- add_subplot(rows,cols,index)

# Figure - represents the entire area where your data visualizations will be displayed

#Axes is like an individual plot or chart within the figure
#g. line charts, bar graph, scatter plot


#Add subplots to the figure
fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

plt.show()

