def find_max(temp, maxlen) :
    if len(temp) > maxlen :
        maxlen = len(temp)
        perm = temp
    elif len(temp) == maxlen :
        if perm < temp :
            perm = temp
    return maxlen

def for_asc(ss):
    for x in range(len(ss)) :
        temp = []
        temp.append(ss[x])
        last = ss[x]
        for y in ss[x+1:] :
            if ord(y) >= ord(last) :
                temp.append(y)
                last = y
        find_max(temp)
        del(temp)

def for_desc(ss, maxlen):
    for x in range(len(ss)) :
        temp = []
        temp.append(ss[x])
        last = ss[x]
        for y in ss[x+1:] :
            if ord(y) <= ord(last) :
                temp.append(y)
                last = y
        maxlen = find_max(temp, maxlen)
        del(temp)

    
perm = []
maxlen = 0
ss = list(input())
#for_asc(ss)
for_desc(ss, maxlen)
print(''.join(perm))
    
