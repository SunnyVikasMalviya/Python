Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import hashlib
>>> print(hashlib.algorithms_gauranteed, end = ' ')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(hashlib.algorithms_gauranteed, end = ' ')
AttributeError: module 'hashlib' has no attribute 'algorithms_gauranteed'
>>> print(hashlib.algorithms_guaranteed, end = ' ')
{'md5', 'shake_128', 'sha3_512', 'sha256', 'blake2s', 'sha384', 'shake_256', 'sha3_224', 'sha1', 'sha224', 'sha3_384', 'sha512', 'sha3_256', 'blake2b'} 
>>> 
