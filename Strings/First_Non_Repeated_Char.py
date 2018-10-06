# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 14:55:27 2018

@author: Sunny
"""

#Function to find first non repeated character in a string
def first_non_repeated_char(word):
    #Dictionary Storing all the characters and their counts 
    chars_in_word = {}
    if len(word) != 0:
        #Initializing Dictionary
        for x in word :
            if x not in chars_in_word :
                chars_in_word[x] = 1
            else :
                chars_in_word[x] += 1
        #Looking for first non repeated Character
        for x in chars_in_word :
            if chars_in_word[x] == 1 :
                return x
        else :
            return "No unrepeated characters"
    else :
        return "No characters present"

print(first_non_repeated_char("abcda"))   #For Debugging