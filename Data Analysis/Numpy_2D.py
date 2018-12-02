import numpy as np

a = [[11, 12, 13], [21, 22, 23], [31, 32, 33], [41, 42, 43]]
A = np.array(a)
print(A.ndim)   #Should return 2
#It will return the dimensions of the array
#Here its 2D
#It will only return 2D when the elements of the outer list are of same\
#size i.e. inner lists should have the same size, else it will return 1D
print(A.shape)    #Should return (4, 3)
#Returns shape i.e. size in each dimension.
print(A.size)    #Should return 9
#Returns the total size of the array
'''
Accessing particular elements in the array
'''
print(A[1][2])  #should return 23
print(A[1])     #Should return [21, 22, 23]
'''
Slicing the array
'''
print(A[0, 0:2])   #Should return [11, 12]
print(A[0:3, 2])   #Should return [13, 23, 33]
'''
Operations on 2D arrays or matrices
'''
#Addition, Subtraction, Hadamard product or Hadamard division
X = np.array([[2, 6], [1, 4]])
Y = np.array([[6, 2], [1, 2]])
Z = X + Y        #Replace + by -, * or /
print(Z)

#Multiplication or division by a scalar
print(Z * 2)

'''
Matrix Multiplication
'''
#The number of columns of first matrix should be equal to the number \
#of rows of the second matrix
#In numpy, the dot function is used to perform matrix multiplication
X = [[1, 2, 3], [1, 3, 6]]
Y = [[1, 2], [3, 1], [3, 6]]
XY = np.dot(X, Y)    #XY is the product of X and Y
print(XY)


