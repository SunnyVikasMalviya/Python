#TIME-IT

"""
timeit measures the amount of time it takes for a certain code snippet to run
It runs the code a large number of times to give the average value of the
time taken hence it is better to use timeit rather than the below code


start = time.time()
#your code snippet here
total = time.time() - start

This gives the time required to complete with all the background process being
still working that might have slowed down the process and hence you might get
a wrong answer.  %timeit does some clever things under the hood to prevent
system calls from interfering with the timing. For example, it prevents cleanup
of unused Python objects (known as garbage collection) which might otherwise
affect the timing.

YOU HAVE TO COPY ALL THE CODE THAT IS REQUIRED TO BE TIMED as timeit can be
considered to be running on its own processor and it will not take codes from
outside its parameters.
The parameter number=5000 determines how many times you want your code to be run
and so you can find the value for a single run by dividing the result of timeit
by number argument.
"""

import timeit

#TIME-IT ON GENERATOR
print("TIMEIT ON GENERATORS(running 5000 times)", end=' ')
print(timeit.timeit('''
input_list = range(100)

def div_by_five(num):
    if num % 5 == 0:
        return True
    else :
        return False

xyz_generator = (i for i in input_list if div_by_five(i))
''', number=5000))
#for x in xyz_generator:
#    print(x, end = '\n')

#TIME-IT ON LIST COMPREHENSION
print("TIMEIT ON LIST COMPREHENSION(running 5000 times)", end=' ')
print(timeit.timeit('''
input_list = range(100)

def div_by_five(num):
    if num % 5 == 0:
        return True
    else :
        return False

xyz_list = [i for i in input_list if div_by_five(i)]
''', number=5000))


"""
OUTPUT

TIMEIT ON GENERATORS(running 5000 times) 0.012581008814519823
TIMEIT ON LIST COMPREHENSION(running 5000 times) 0.2024676748677462

"""
