'''
Code Jam 2020 Qualification Round 2nd Question Solution
'''

class Nesting_Depth(object):
    def __init__(self, S):
        self.S = S
        self.S_ = ''
        return
    def add_paren(self):
        temp = ''
        for x in self.S:
            x = int(x)
            temp = x*'(' + str(x) + x*')'
            self.S_ += temp
        return self.S_
    def remove_xtra_paren(self):
        while len(''.join(self.S_.split(')('))) < len(self.S_):
            self.S_ = ''.join(self.S_.split(')('))
        return self.S_
    def find_S_(self):
        self.S_ = self.add_paren()
        self.S_ = self.remove_xtra_paren()
        return self.S_

test = int(input())
obj = []
for t in range(test):
    S = input()
    ob = Nesting_Depth(S)
    obj.append(ob)
    
for t in range(test):
    S_ = obj[t].find_S_()
    print("Case #{}: {}".format(t+1, S_))
