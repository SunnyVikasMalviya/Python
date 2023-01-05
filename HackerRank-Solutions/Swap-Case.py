def swap_case(s):
    swappedString = ""
    for _ in s:
        if _.isalpha():
            if _.islower():
                _ = _.upper()
            else:
                _ = _.lower()  
        swappedString = swappedString + _
    return swappedString

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
