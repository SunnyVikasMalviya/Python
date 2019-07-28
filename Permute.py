a = []
def actual_permute(arr, l, r):
    """
    The actual_permute function takes a list and indices of its first and last
    elements and returns all the permutations of the list elements to the permute
    function which in turn returns it to the user.
    """
    if l == r :
        a.append(''.join(arr))
    else :
        for i in range(l, r+1):
            arr[l], arr[i]  = arr[i], arr[l]
            actual_permute(arr, l+1, r)
            arr[l], arr[i]  = arr[i], arr[l]
    return a

def permute(arr):
    """
    The permute function uses actual_permute function to find the permutations
    of the list elements by taking only the list from the user and then passing
    it to the actual_permute function with indices of the first and last elements
    of the list.
    permute function was made in order to transfer the responsibility of
    finding and passing the indices of the first and last elements from user to
    itself as the actual_permute function requires all the three parameters.
    """
    a = actual_permute(arr, 0, len(arr)-1)
    return a


#For Debugging
#arr = []
#arr = input().split(' ')
#a = permute(arr)
#print(a)
"""
INPUT

a b c

OUTPUT

abc
acb
bac
bca
cba
cab
"""
