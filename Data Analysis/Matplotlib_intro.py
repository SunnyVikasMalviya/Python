from matplotlib import pyplot as plt


x = [5, 6, 7, 8]
y = [7, 3, 8, 3]


plt.plot(x, y, color = (0.2, 0.22, 0.95, 0.2))   #RGBA values

plt.title('Epic Chart')
plt.ylabel('Some other thing')
plt.xlabel('Something')
plt.show()
