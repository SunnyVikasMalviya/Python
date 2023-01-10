def print_rangoli(size):
    '''
    Function to print alphabetical pattern for a given size.
    '''
    #Getting all alphabets required in a list.
    alphabets = []
    for i in range(97, 97+size):
        alphabets.append(chr(i))
    
    #Initializing number of rows, columns, left and right ptrs, and empty list to store pattern strings
    row = size*2-1
    col = row*2-1
    pat = [""] * row
    lptr, rptr = row//2, row//2
    
    #Creating pattern starting from the middle, moving lptr and rptr towards left and right
    for i in range((row//2)+1):
        line = list(reversed(alphabets[i+1:size])) + alphabets[i:size]
        line = "-".join(line).center(col, '-')
        pat[lptr] = line
        pat[rptr] = line
        lptr = lptr-1
        rptr = rptr+1
    print("\n".join(pat))
    return        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
