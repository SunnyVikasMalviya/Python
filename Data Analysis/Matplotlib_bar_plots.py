from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [5, 6, 7, 8]
y = [7, 3, 8, 3]

x2 = [3, 4, 9, 1]
y2 = [5, 6, 2, 2]

plt.bar(x, y, align = 'center', color = 'c')   
plt.bar(x2, y2, align = 'center', color = 'y')

plt.title('Epic Chart')
plt.ylabel('Some other thing')    
plt.xlabel('Something')           

plt.show()                        



