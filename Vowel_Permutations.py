def makPerms(l1 = {}):
    l2 = {'a' : 0, 'e' : 0, 'i' : 0, 'o' : 0, 'u' : 0}
    for x in l1:
        if x == 'a':
            l2['e'] += l1[x]
        elif x == 'e':
            l2['a'] += l1[x]
            l2['i'] += l1[x]
        elif x == 'i':
            l2['a'] += l1[x]
            l2['e'] += l1[x]
            l2['o'] += l1[x]
            l2['u'] += l1[x]
        elif x == 'o':
            l2['i'] += l1[x]
            l2['u'] += l1[x]
        elif x == 'u':
            l2['a'] += l1[x]
    l1 = l2
    return l1

l1 = {'a' : 1, 'e' : 1, 'i' : 1, 'o' : 1, 'u' : 1}
l1 = makPerms(l1)
l1 = makPerms(l1)
#l1 = makPerms(l1)
l1 = makPerms(l1)
su = 0
for x in l1 :
    su = su + l1[x]
print(su)
