def eqn_solver(eqn):
    if 'divide' in eqn:
        pos = eqn.index('divide')
        res = int(eqn[pos-1])/ int(eqn[pos+1])
        eqn[pos] = res
        eqn.pop(pos-1)
        eqn.pop(pos)
        
    if 'multiply' in eqn:
        pos = eqn.index('multiply')
        res = int(eqn[pos-1])* int(eqn[pos+1])
        eqn[pos] = res
        eqn.pop(pos-1)
        eqn.pop(pos)
        
    if 'add' in eqn:
        pos = eqn.index('add')
        res = int(eqn[pos-1])+ int(eqn[pos+1])
        eqn[pos] = res
        eqn.pop(pos-1)
        eqn.pop(pos)
        
    if 'subtract' in eqn:
        pos = eqn.index('subtract')
        res = int(eqn[pos-1])- int(eqn[pos+1])
        eqn[pos] = res
        eqn.pop(pos-1)
        eqn.pop(pos)
    return(eqn[0])

#For Debugging
#print(eqn_solver(['4', 'divide', '2', 'add', '6', 'multiply', '6', 'subtract', '9']))
#eqn = []
#eqn = input().split(' ')
#print(eqn_solver(eqn))
'''
INPUT
4 add 2 multiply 6 divide 2 subtract 3

OUTPUT
['4', 'add', '2', 'multiply', '6', 'divide', '2', 'subtract', '3']
7
'''

