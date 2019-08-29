import hashlib

def hashing(word) :
    """
    The hashing function takes a string input and converts it into a hash using
    the SHA256 hashing technique present in the hashlib library in python.
    Arguments
    word : a string
    Return Value
    ans : a string of hexadecimal digits corresponding to the SHA256 hashing
    of the given word.
    """
    ans = hashlib.sha256(word.encode())
    return ans.hexdigest()

if __name__ == '__main__' :
    print(hashing("Hello World!!!"))



"""
INPUT

Hello World!!!

OUTPUT


"""
