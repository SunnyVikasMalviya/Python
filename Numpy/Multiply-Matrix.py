import numpy as np

N = int(input())
 
A = np.array([input().split() for _ in range(N)], int)
B = np.array([input().split() for _ in range(N)], int)
print(np.dot(A, B))


"""
Input format:

2
1 2
3 4
2 6
3 5

"""
