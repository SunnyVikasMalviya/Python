from Prime_Check import is_prime

def Mersenne_prime(n):
    """
    In mathematics, a Mersenne Prime is a prime number that is one less than a
    power of 2  i.e. M(n) = 2^n - 1 should be prime for some n.
    The Mersenne_prime function takes a integer argument which is n in M(n) and
    returns a list of Mersenne prime numbers.
    """
    lst = []
    for x in range(n):
        num = (2**x)-1
        if is_prime(num):
            lst.append(num)
    return lst

#For Debugging
try :
    print(Mersenne_prime(int(input())))
except ValueError :
    print("Enter Positive Integers Only")

"""
INPUT

31(Maximum Input)

OUTPUT

[3, 7, 31, 127, 8191, 131071, 524287]
"""
