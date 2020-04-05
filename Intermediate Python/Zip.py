'''
The zip function takes values from multiple iterables and aggregates them into
single unit (which is a zip object) where they share the same index.
'''

x = [1, 2, 3, 4]
y = [7, 6, 4, 1]
z = ['a', 'b', 'p', 'z']

for a,b,c in zip(x, y, z):
    print(a, b, c)          #Output 1

print()
#the above can also be done as follows

for i in zip(x, y, z):
    print(i)                #Output 2
print()
print(zip(x,y,z))           #Output 3

print()

w = ['p', 'q']
[print(i) for i in zip(w,x,y,z)]        #Output 4

print()

print(dict(zip(x, y)))      #Output 5
#with just two iterables, zip() can be combined with dict() to form a key value
#pair

print()

#List comprehension with zip()
[print(x, y, z) for x, y ,z in zip(x, y, z)]    #Output 6
print(x)
'''
The x remains same as declared at the top because of the following reason:
Here the use of x,y,z as both iterables and loop variables will work as the
loop variables are just temporary in list comprehension; but its not the case
with for loops, so x,y,z cannot be used as looping variables for iterables
of the same name.
So, if we try to print x after using it as looping variable, its value will change.
'''

print()

for x, y, z in zip(x, y, z):
    print(x, y, z)
print(x,y,z)                #Output 7


'''
1. Each element in a zip object is a tuple of elements present at the same index
of all the parameters in the zip().
2. If the parameters in zip() have different lengths, the zip object will have
length of the smallest parameter; rest of the elements in the larger lengths will
be truncated.
'''






#OUTPUT
'''
#Output 1
1 7 a
2 6 b
3 4 p
4 1 z

#Output 2
(1, 7, 'a')
(2, 6, 'b')
(3, 4, 'p')
(4, 1, 'z')

#Output 3
<zip object at 0x000001EA91685088>

#Output 4
('p', 1, 7, 'a')
('q', 2, 6, 'b')

#Output 5
{1: 7, 2: 6, 3: 4, 4: 1}

#Output 6
1 7 a
2 6 b
3 4 p
4 1 z
[1, 2, 3, 4]

#Output 7
1 7 a
2 6 b
3 4 p
4 1 z
4 1 z

'''
