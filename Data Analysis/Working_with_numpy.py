import numpy as np
import time

#Below we have a list of numbers and we are casting it to a numpy array
#This is one way of creating a numpy array or ndarray.
a = np.array([40, 50, 70, 30, 90 ])
print(a[1])
print(a)

type(a)    #Should return numpy.ndarray
a.dtype    #should return int32 meaning 32 bit integer
print(a.dtype)
print(a.size)   #returns the size of the ndarray.
print(a.ndim)   #returns the number of dimensions the ndarray has.
print(a.shape)  #returns the size in each dimension of the  ndarray.
'''
Numpy arrays have all element of the same datatype.
Numpy arrays have fixed size.
Numpy are the basis of pandas
'''

b = np.array([.03, 33.4, 1.2])
print(b.dtype)    #should return float64

'''
Slicing
'''
c = b[1:4]  #Elements with indices 1 2 and 3 are stored in c
c[1:3] = 300 #Elements 1 and 2 are now 300 and 400 respectively
print(c)

"""
NUMPY ARRAYS vs LISTS
"""

#Addition & Subtraction and HADAMARD(element to element) \
#Product & Division
u = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
v = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
z = []
start = time.time()
for n, m in zip(u, v):
    z.append(n + m)     #Replace + with -, * or /
print(z)
print(time.time() - start)  #0.004990339279174805

start = time.time()
u = np.array([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])
v = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
z = u + v               #Replace + with -, * or /
print(z)
print(time.time() - start)  #0.0029935836791992188

'''For small inputs lists are faster, but as the input size grows
arrays obviously takes lead.'''

#Scalar Addition, Subtraction, Multiplication & Division
#Whatever is done is done to each element of the list or array. This \
#property is known as broadcasting
u = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
z = []

for n in u:
    z.append(2 + n)     #Replace + with -, * or /
print(z)

u = np.array([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])
z = 2 + u               #Replace + with -, * or /
print(z)

#Dot Product
u = np.array([1, 2])
v = np.array([3, 2])
res = np.dot(u, v)
print(res)


'''
Universal Functions : Functions that apply to the whole array like \
mean, median, mode, max, min
'''

a = np.array([1, 2, 4, -3])
mean_a = a.mean()
max_a = a.max()
print(mean_a)
print(max_a)

np.pi   #Refers to pi = 22/7
x = np.array([0, np.pi/2, np.pi])   # x = [0, pi/2 , pi]
y = np. sin(x)     # y = [sin(0), sin(pi/2), sin(pi)] = [0, 1, 0]
print(y)

'''
Line Space
'''
a = np.linspace(-2, 2, num = 9)
#The number line from -2 to 2 is split into 9  equal parts and \
#the extreme values of the parts is returned
print(a)

    
