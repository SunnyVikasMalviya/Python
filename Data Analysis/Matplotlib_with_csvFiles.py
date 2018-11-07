from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np


style.use('ggplot')

x, y = np.loadtxt('graph.csv', unpack = True, delimiter = ',')
#The file is read till the end because of the unpack attribute
#x and y are lists that store the values from the file

plt.plot(x, y)
plt.title('Not important')
plt.xlabel('X axis of a not so important graph')
plt.ylabel('Y axis of a not so important graph')

plt.show()
