#Method 1
def reverseArray(a):
    """
    Function to reverse an array. Time Complexity O(n).
    Limitation: Linear time complexity. Additional space required to store new array.
    """
    b = [0] * len(a)
    for i in range(len(a)):
        b[-i-1] = a[i]
    return b

#Method 2
def reverseArray(a):
    """
    Function to reverse an array. Time Complexity O(log n).
    Limitation: Can only be used for numerical arrays.
    """
    n = len(a)
    for i in range(n//2):
        #Swapping extreme elements in the same array
        a[i] = a[i] + a[n-i-1]
        a[n-i-1] = a[i] - a[n-i-1]
        a[i] = a[i] - a[n-i-1]    
    return a
