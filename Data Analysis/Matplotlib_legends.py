from matplotlib import pyplot as plt
#from matplotlib import style

x = [5, 6, 7, 8]
y = [7, 3, 8, 3]

x2 = [3, 7, 9, 1]
y2 = [5, 6, 2, 0]

plt.scatter(x, y, color = 'c')   
plt.scatter(x2, y2, color = 'g')

plt.title('Epic Chart')
plt.ylabel('Some other thing')    
plt.xlabel('Something')           
#plt.legend()
#plt.grid(True, color = 'k')

plt.show()                        



