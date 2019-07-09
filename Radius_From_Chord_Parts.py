"""
Program for finding chord lengths or radius when two intersecting chords
are given with their lengths.

formula :
4r^2 = x^2 + y^2 + z^2 + w^2
where r = radius
x = 1st part of chord one
y = 2nd part of chord one
z = 1st part of chord two
w = 2nd part of chord two
"""

def finding_fourth_part(x, y, z):
    w = (x * y) / z
    return w

def finding_radius(x, y, z, w):
    r = (((x**2) + (y**2) + (z**2) + (w**2)) / 4)**0.5
    return r
    
a = int(input("How many chord parts do you know?"))
if a <= 2 or a > 4:
    print("More than two chord parts should be known.")
elif a == 3:
    print("Enter the known three chord parts:")
    x = int(input())
    y = int(input())
    z = int(input())
    w = finding_fourth_part(x, y, z)
    r = finding_radius(x, y, z, w)
    print("Radius : {}".format(r))
    
else :
    print("Enter the known four chord parts:")
    x = int(input())
    y = int(input())
    z = int(input())
    w = int(input())
    r = finding_radius(x, y, z, w)
    print("Radius : {}".format(r))
