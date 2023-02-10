def reverseArray(a):
    """
    Function to reverse an array.
    """
    b = [0] * len(a)
    for i in range(len(a)):
        b[-i-1] = a[i]
    return b
