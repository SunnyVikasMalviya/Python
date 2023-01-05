def count_substring(string, sub_string):
    '''
    Function to count number of times a substring occurs in a string.
    '''
    n = len(string)-len(sub_string)+1
    cnt = 0
    for _ in range(n):
        if string[_:_+len(sub_string)] == sub_string:
            cnt = cnt+1
    return cnt

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
