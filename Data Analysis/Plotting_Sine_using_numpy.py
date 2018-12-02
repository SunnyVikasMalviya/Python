from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')


x = np.linspace(0, 2*np.pi, 5)
#Increase the third argument to make the graph smoother
y = np.sin(x)

x2 = np.linspace(0, 2*np.pi, 20)
y2 = np.sin(x2)

plt.plot(x, y, color = 'red', label = "For 5 splits")
plt.plot(x2, y2, color = 'blue', label = "For 20 splits")
plt.xlabel("Angle")
plt.ylabel("Value")
plt.title("Sine Graph")
plt.legend()
plt.show()
