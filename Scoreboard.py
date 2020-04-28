"""

"""








N_Bits = {}
BSD = {0: (['1', '1', '1', '0', '1', '1', '1'], (0, 1, 2, 4, 5, 6)), \
       1: (['0', '0', '1', '0', '0', '1', '0'], (2, 5)), \
       2: (['1', '0', '1', '1', '1', '0', '1'], (0, 2, 3, 4, 6)), \
       3: (['1', '0', '1', '1', '0', '1', '1'], (0, 2, 3, 5, 6)), \
       4: (['0', '1', '1', '1', '0', '1', '0'], (1, 2, 3, 5)), \
       5: (['1', '1', '0', '1', '0', '1', '1'], (0, 1, 3, 5, 6)), \
       6: (['1', '1', '0', '1', '1', '1', '1'], (0, 1, 3, 4, 5, 6)), \
       7: (['1', '0', '1', '0', '0', '1', '0'], (0, 2, 5)), \
       8: (['1', '1', '1', '1', '1', '1', '1'], (0, 1, 2, 3, 4, 5, 6)), \
       9: (['1', '1', '1', '1', '0', '1', '1'], (0, 1, 2, 3, 5, 6))}

digit_n_needs = []

def gps(rem_segs, ind = 0):
    if ind == len(digit_n_needs):
        return -2
    for dig, req in zip(digit_n_needs[ind][0], digit_n_needs[ind][1]):
        if req > rem_segs:
            continue
        elif req == rem_segs:
            res = gps(rem_segs - req, ind +1)
            if  res == -2:
                return dig
            if res == -1:
                continue
            res = dig * (10**(len(digit_n_needs)-ind-1)) + res
            return res
        elif req < rem_segs:
            res = gps(rem_segs - req, ind +1)
            if res == -2:
                continue
            if res == -1:
                continue
            res = dig * (10**(len(digit_n_needs)-ind-1)) + res
            return res            
    else:
        return -1

def gps1(rem_segs, ind=0):
    print("gps({}, {})".format(ind, rem_segs))
    print("Checking if last+1 digit")
    if ind == len(digit_n_needs):
        print("Returning -2 since it is last+1 digit")
        return -2
    print("Entering loop for {} digit".format(ind))
    for dig, req in zip(digit_n_needs[ind][0], digit_n_needs[ind][1]):
        if req > rem_segs:
            print("{} > {}".format(req, rem_segs))
            continue
        elif req == rem_segs:
            res = gps1(rem_segs - req, ind+1)
            if  res == -2:
                print("Returning {}".format(dig))
                return dig
            if res == -1:
                continue
            res = dig * (10**(len(digit_n_needs)-ind-1)) + res
            print("Returning {}".format(res))
            return res
        elif req < rem_segs:
            res = gps1(rem_segs - req, ind+1)
            if res == -2:
                continue
            if res == -1:
                continue
            res = dig * (10**(len(digit_n_needs)-ind-1)) + res
            print("Returning {}".format(res))
            return res            
    else:
        print("Returning List {} end -1".format(ind))
        return -1

def possible_digits():
    for key, value in N_Bits.items():
        tup = value[1]
        poss_digs = []
        req_segs = []
        for dig, segs in BSD.items():
            if set(tup).issubset(set(segs[1])):
                poss_digs.append(dig)
                req_segs.append(len(segs[1])-len(tup))
        digit_n_needs.append((poss_digs[::-1], req_segs[::-1]))
    return digit_n_needs

def indexing_glowing_segments():
    for key, value in N_Bits.items():
        tup = ()
        for index, segment in enumerate(value):
            if segment == '1':
                tup += tuple([index])
        N_Bits[key] = tuple([value, tup])
    return N_Bits
        

def main():
    inp = input().split()
    n, k = int(inp[0]), int(inp[1])
    for i in range(n):
        digit = list(input())
        N_Bits[i] = digit
    indexing_glowing_segments()
    possible_digits()
    #display_inputs()
    print(gps(k))

def display_inputs():
    for x,y in N_Bits.items():
        print(x,y)

if __name__ == "__main__":
    main()
#MVik
