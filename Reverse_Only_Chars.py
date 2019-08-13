def reverse_only_chars(word) :
    l = 0
    r = len(word)-1
    while l<r :
        if not word[l].isalpha() :
            l+=1
            continue
        if not word[r].isalpha() :
            r-=1
            continue
        word[l], word[r] = word[r], word[l]
        l+=1
        r-=1
    return word

#For Debugging
if __name__ == '__main__':
    word = list(input())
    print(''.join(reverse_only_chars(word)))


"""
INPUT

a?b>cd@<f5

OUTPUT

f?d>cb@<a5
"""
