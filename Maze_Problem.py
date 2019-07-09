#MAZE PROBLEM
"""
A matrix or maze has been given and we need to find the number of paths from
the starting postion to the end node.
Requirment: If starting position is (1,1) then just the destination is required.
    If starting postion is not (1,1) then both starting and ending postions are
    required.
Matrix Dimensions : MxN
Starting Postion : (x1, y1)
Destination : (x2, y2)
"""

from math import factorial, trunc 

def find_number_of_paths(pos):
    num_paths = factorial(pos[0]+pos[1]-2) / (factorial(pos[0]-1)*factorial(pos[1]-1))
    return num_paths

a = int(input("Startng position is (1, 1)?(True = 1, False = 0):"))
if a == 1:
    print("Enter Ending Postion:")
    dest = tuple(int(x.strip()) for x in input().split(','))
    num_paths = find_number_of_paths(dest)
    print("Number of paths from (1,1) to {} : {}".format(dest, trunc(num_paths)))
elif a == 0:
    print("Enter Starting Postion:")
    start = tuple(int(x.strip()) for x in input().split(','))
    print("Enter Ending Postion:")
    dest = tuple(int(x.strip()) for x in input().split(','))
    num_paths = find_number_of_paths((dest[0]-start[0]+1, dest[1]-start[1]+1))
    print("Number of paths from {} to {} : {}".format(start, dest, trunc(num_paths)))
else :
    print("Invalid Input")


'''
For printing factorial
import math
print(math.factorial(4))
'''


#OUTPUT
"""
Startng position is (1, 1)?(True = 1, False = 0):0
Enter Starting Postion:
2,2
Enter Ending Postion:
5,5
Number of paths from (2, 2) to (5, 5) : 20
"""
