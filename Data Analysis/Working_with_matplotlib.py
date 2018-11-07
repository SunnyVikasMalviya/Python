from matplotlib import pyplot as plt
from matplotlib import style

x = [5, 6, 7, 8]
y = [7, 3, 8, 3]

x2 = [3, 7, 9, 1]
y2 = [5, 6, 2, 0]

print(len(x))
print(len(y))
print(len(x2))
print(len(y2))

plt.plot(x, y, 'g', linewidth = 5, label = 'line One')    #label is the legend
plt.plot(x2, y2, 'c', linewidth = 2, label = 'line Two')

plt.title('Epic Chart')
plt.ylabel('Some other thing')    
plt.xlabel('Something')           
plt.legend()      #used to display the legends of a graph.
#Adding label argument to the plot makes the legends but doesn't display it.
#We have to call the legend() in order to display the lengends
plt.grid(True, color = 'k')    #Used to represent the grid; k stands for black

plt.show()                        



