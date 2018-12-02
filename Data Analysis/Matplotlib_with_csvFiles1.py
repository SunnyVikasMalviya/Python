from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np


style.use('ggplot')

x, y, z = np.loadtxt('graph1.csv', unpack = True, delimiter = ',')
#The unpack attribute splits the inputs from the file into parts divided \
#by the delimiter. MUST unpack the exact same number of columns that will\
#come from the delimiter that you state.
#x and y are numpy arrays(not lists) that store the values from the file

print(x)
print(y)
print(z)
plt.plot(x, y, z, y)
plt.title('Not important')
plt.xlabel('X axis of a not so important graph')
plt.ylabel('Y axis of a not so important graph')

plt.show()
