from matplotlib import pyplot as plt
from matplotlib import style
#Premade style sheets are available for matplotlib
#they have .mplstyle extension
#They are similar to css for html


x = [5, 6, 7, 8]
y = [7, 3, 8, 3]

x2 = [3, 7, 9, 1]
y2 = [5, 6, 2, 0]

print(len(x))
print(len(y))
print(len(x2))
print(len(y2))

help(style)      #Just to see the available styles
style.use('my_style')     #Used to use a specific type of style

plt.plot(x, y)
plt.plot(x2, y2)

plt.title('Epic Chart')
plt.ylabel('Some other thing')    
plt.xlabel('Something')           
plt.show()                        



#C:\Users\Sunny\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\matplotlib\mpl-data\stylelib
#The above address contains all the styles available for styling

