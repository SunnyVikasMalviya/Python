#Enumerate
'''The enumerate function returns a tuple containing the count, and then the
actual value from the iterable.'''
example = ['Up', 'Right', 'Down', 'Left']

for i in range(len(example)):
    print(i, example[i])

#The above can be done using enumerate
for i, j in enumerate(example):
    print(i, j)

new_dict = dict(enumerate(example))

print(new_dict)

[print(i, j) for i, j in enumerate(new_dict)]

example_dict = {'left':'<', 'right':'>', 'up':'^', 'dance':'\/'}

[print(i, j) for i,j in enumerate((example_dict, example_dict.values()))]
