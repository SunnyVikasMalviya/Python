def circle_pattern(n):
    mat = [[n for x in range(2*n-1)] for y in range(2*n-1)]
    if n == 1:
        return mat
    else :
        mat1 = circle_pattern(n-1)
        for x in range(2*(n-1)-1):
            for y in range(2*(n-1)-1):
                mat[x+1][y+1] = mat1[x][y]
    return mat
    
#For Debugging
#n = int(input())
#print(circle_pattern(n))


"""
INPUT
4

OUTPUT
[[4, 4, 4, 4, 4, 4, 4], \
[4, 3, 3, 3, 3, 3, 4], \
[4, 3, 2, 2, 2, 3, 4], \
[4, 3, 2, 1, 2, 3, 4], \
[4, 3, 2, 2, 2, 3, 4], \
[4, 3, 3, 3, 3, 3, 4], \
[4, 4, 4, 4, 4, 4, 4]]
"""
