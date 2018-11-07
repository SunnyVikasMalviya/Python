from matplotlib import pyplot as plt


x = [5, 6, 7, 8]
y = [7, 3, 8, 3]

#The below 2 statements display the size of the two lists
#These lines are used for debugging the code out of ValueError : x and y must \
#have same first dimension. The below two lines just display the lengths, the \
#task of changing the lengths of the variables still lies with the programmer.
print(len(x))
print(len(y))


plt.plot(x, y, color = (0.2, 0.22, 0.95, 0.2))
#RGBA values
#Can also write like : color = 'y'
#here y stands for yellow
#The fourth value defines the transparency of the graph
#All the values should be between 0 to 1


plt.title('Epic Chart')
plt.ylabel('Some other thing')    #Naming the y axis
plt.xlabel('Something')           #Naming the x axis
plt.show()                        #Display the plot


