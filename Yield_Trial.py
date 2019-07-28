def yield_trial(a, b):
    """
    Yield is used to goback to the calling function. The yielded result is saved
    in an object and the  yield saves enough state in the function so that when
    it is called again, the function can continue its operations from the statement
    where it yielded previously, unlike return that makes the function execute again
    from the very beginning.
    The yield_trial function yields the results of basic arithmetic operation
    performed on the two input arguments it takes.Using yield, it returns a
    different result everytime it is called and the yielded value is stored in an
    object.
    """
    yield ("Sum of {} and {} : {}".format(a, b, a+b))
    a = a + 1
    b = b + 1
    yield ("Difference of {} and {} : {}".format(a, b, a-b))
    a = a + 1
    b = b + 1
    yield ("Product of {} and {} : {}".format(a, b, a*b))
    a = a + 1
    b = b + 1
    yield ("Quotient of {} and {} : {}".format(a, b, a/b))
    a = a + 1
    b = b + 1
    yield ("Remainder of {} and {} : {}".format(a, b, a%b))
    a = a + 1
    b = b + 1     
    yield "All operation are over. Final value of a is {} and b is {}".format(a, b)

#For Debugging
#a = int(input("Enter value of a:"))
#b = int(input("Enter value of b:"))
#for x in yield_trial(a, b):
#    print(x)
#print(a, b)

"""
INPUT

Enter value of a:4
Enter value of b:2

OUTPUT

Sum of 4 and 2 : 6
Difference of 5 and 3 : 2
Product of 6 and 4 : 24
Quotient of 7 and 5 : 1.4
Remainder of 8 and 6 : 2
All operation are over. Final value of a is 9 and b is 7
"""
