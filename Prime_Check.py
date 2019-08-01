def is_prime(num):
    """
    Takes a number argument and returns boolean result based on whether the
    number is prime or not.
    """
    try :
        if num < 2:
            return False
        elif num == 2:
            return True
        elif num % 2 == 0:
            return False
        else :
            i = 3
            while i < (num / 2):
                if num % i == 0:
                    return False
                else :
                    i += 2
            else :
                return True
    except TypeError :
        return False

#For Debugging
#try :
#    print(is_prime(int(input())))
#except ValueError :
#    print(False)

"""
INPUT & OUTPUT

2
True
3
True
4
False
5
True
6
False
7
True
8
False
9
False

"""
