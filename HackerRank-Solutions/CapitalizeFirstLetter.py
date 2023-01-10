def CapitalizeFirstLetter(s):
    '''
    Function to capitalize first letter of all the words in a sentence passed as string.
    '''
    words = s.split(" ")
    cap_words = []
    for word in words:
        cap_words.append(word.capitalize())
    s = " ".join(cap_words)
    return s

if __name__ == "__main__":
    s = input()
    print(CapitalizeFirstLetter(s))
