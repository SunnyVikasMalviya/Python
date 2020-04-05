'''
Google Code Jam 2020 Qualification Round 1st Question 
'''
class mat(object):
    def __init__(self, n, arr):
        self.n = n
        self.arr = arr
        return
    def find_k(self):
        k = 0
        for i in range(self.n):
            for j in range(self.n):
                if i == j:
                    k += self.arr[i][j]
        return k
    def find_r(self):
        r = 0
        for i in range(self.n):
            if len(set(self.arr[i])) != self.n:
                r += 1
        return r
    def find_c(self):
        c = 0
        for j in range(self.n):
            temp = []
            for i in range(self.n):
                temp.append(self.arr[i][j])
            if len(set(temp)) != self.n:
                c += 1
        return c

test = int(input())
obj = []
for t in range(test):
    n = int(input())
    arr = []
    for i in range(n):
        temp = input().split(' ')
        temp = [int(x) for x in temp]
        arr.append(temp)
    ob = mat(n, arr)
    obj.append(ob)

for t in range(test):
    k = obj[t].find_k()
    r = obj[t].find_r()
    c = obj[t].find_c()
    print("Case #{}: {} {} {}".format(t+1, k, r, c))
