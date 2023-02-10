def getPossibleGridCoordinates(x, y, z, n):
    """
    Function to print grid coordinates within the given cuboid dimensions.
    Constraint: Sum of grid coordinates should not be equal to the given value n.
    """
    print([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n])

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    getPossibleGridCoordinates(x, y, z, n)
