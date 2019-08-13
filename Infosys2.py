def anchor_points(arr) :
    apl = []
    if a[0] > a[1] :
        inc = 0
    else :
        inc = 1
    apl.append(0)
    
    for x in range(len(arr)-2) :
        if inc == 0 :
            if arr[x+1] < arr[x+2] :
                apl.append(x+1)
                inc = 1
        else :
            if arr[x+1] > arr[x+2] :
                apl.append(x+1)
                inc = 0
    apl.append(len(arr)-1)
    print(apl)
    maxapl = 0
    maxs = 0
    maxy = 0
    for x in range(len(apl)-1):
        if apl[x+1] - apl[x] > maxapl :
            maxapl = apl[x+1] - apl[x]
            maxx = apl[x]
            maxy = apl[x+1]
    for x in arr[maxx: maxy+1]:
        print(x, end = "")
    
            

a = list(input())
a = [int(x) for x in a]
print(a)
if sorted(a) == a:
    print(a[len(a)-1], a[0])
elif reversed(sorted(a)) == a :
    print(a[len(a)-1], a[0])
else :
    anchor_points(a)
