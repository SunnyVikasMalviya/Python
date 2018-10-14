vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
consonents = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', \
		  'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', \
          'Q', 'W', 'R', 'T', 'Y', 'P', 'S', 'D', 'F', 'G', 'H', 'J', 'K', \
          'L', 'M', 'N', 'B', 'V', 'C', 'X', 'Z']
		  
def vowel_consonent_count(word) :
    v_cnt = 0
    c_cnt = 0
    for x in word :
        if x in vowels :
            v_cnt += 1
        elif x in consonents :
            c_cnt += 1
    return v_cnt, c_cnt   #returns a tuple

#(x, y) = vowel_consonent_count('hEllo WooOrld')
		  
#print(x, y)
		  
