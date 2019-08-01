from Prime_Check import is_prime

def prime_in_list(list_):
    """
    The prime_in_list function takes a list argument, iterates through all the
    elements in the list, and returns a list of all the prime numbers in the
    list.
    """
    lst = []
    for x in list_:
        if is_prime(x):
            lst.append(x)
    return lst
    

#For Debugging
#print(prime_in_list([1, 2, 3, 4, 5, 6, 'A', 7, 8, 9]))

"""
INPUT

[1, 2, 3, 4, 5, 6, 7, 8, 9]

OUTPUT

[2, 3, 5, 7]
"""
