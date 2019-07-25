"""
Permutations & Combinations
"""
from itertools import permutations, combinations

arr = []
arr = input("Enter 3 or more elements:").split(' ')
perms = permutations(arr)
combs = combinations(arr,3)

#The functions return an object of the type array, so printing them will display
#<itertools.permutations object at 0x0000015776C92570>
#<itertools.combinations object at 0x0000015776C969A8>

#To print the value of the object, iterate through it
print("Permutations")
for i in perms:
    print(i)
print("Combinations")
for j in combs:
    print(j)

#For more info, visit https://www.geeksforgeeks.org/permutation-and-combination-in-python/

"""
INPUT

Enter 3 or more elements:A B C

OUTPUT

Permutations
('A', 'B', 'C')
('A', 'C', 'B')
('B', 'A', 'C')
('B', 'C', 'A')
('C', 'A', 'B')
('C', 'B', 'A')
Combinations
('A', 'B', 'C')

"""
