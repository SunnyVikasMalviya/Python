def simple_generator_function():
    yield 1
    yield 2
    yield 'A'


#This can also be used
#for x in simple_generator_function():
#    print(x)

x = simple_generator_function()

print(x.__next__()) #In python 2, next() in place of __next__()
print(x.__next__())
print(x.__next__())


"""
A function is automatically a generator function if it contains a yield in it.
For more information on yield or generator function, goto geeksforgeeks.
"""
