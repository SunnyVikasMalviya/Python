'''
Generators
'''
#Generators don't return things, they yield it.
#We will create our own simple generator

def gen_func():
    """
    Simple example of our own generator.
    """
    yield 'Corona Corona'
    yield 'Corona Corona'
    yield 'Corona Corona'
    yield 'Me hun ek Corona'

def normal_func_without_gen():
    """
    A function trying to break the secret combo without using a generator.
    See how many break statements are present to cease the processing and also
    so many logic statements involved.
    """
    found_combo = False
    for c1 in range(10):
        if found_combo:
            break
        for c2 in range(10):
            if found_combo:
                break
            for c3 in range(10):
                if (c1, c2, c3) == correct_combo:
                    print('Found the combo: {}'.format((c1,c2,c3)))
                    found_combo = True
                    break
                print(c1, c2, c3)

def combo_gen():
    """
    Our generator to break the combo.
    """
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield (c1, c2, c3)
                
def with_gen_func():
    """
    A function trying to break the secret combo by using a our own generator
    functoin combo_gen().
    See how only a single break statement is present to cease the processing
    and also only a single logic statement is involved.
    """
    for i in combo_gen():
        print(i)
        if i == correct_combo:
            print("Found the combo: {}".format(i))
            break
    

if __name__ == '__main__' :
    #for i in gen_func():  #means while the func is yielding a value
    #print(i)
    correct_combo = (4, 6, 3)
    print("Finding combo using normal function without Generator.")
    normal_func_without_gen()
    print("\n\n")
    print("Finding combo using function with generator function.")
    with_gen_func()


#OUTPUT
"""
Finding combo using normal function without Generator.
0 0 0
0 0 1
0 0 2
0 0 3
0 0 4
0 0 5
.
.
.
.
.
4 5 8
4 5 9
4 6 0
4 6 1
4 6 2
Found the combo: (4, 6, 3)


Finding combo using function with generator function.
(0, 0, 0)
(0, 0, 1)
(0, 0, 2)
(0, 0, 3)
(0, 0, 4)
(0, 0, 5)
.
.
.
.
.
(4, 5, 9)
(4, 6, 0)
(4, 6, 1)
(4, 6, 2)
(4, 6, 3)
Found the combo: (4, 6, 3)
"""
