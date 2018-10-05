# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 20:18:58 2018

@author: Sunny
"""

#Anagram : Words having all the same characters
#Functions to check whether two strings are anagram of each other or not

'''One method for this is to create both dicts and check their equivalance'''
'''But here i am doing something else'''

def anagram_check(word1, word2):
    if len(word1) == len(word2):
        #dictionary storing all the characters in word1 and their count 
        chars_in_word1 = {}
        #dictionary storing all the characters in word2 and their count
        chars_in_word2 = {}
        
        #Loop to count each letters frequency in the word1 and add it to dict
        for x in word1 :
            if x not in chars_in_word1:
                chars_in_word1[x] = 1
            else :
                chars_in_word1[x] = chars_in_word1[x] + 1
        #Loop to count each letters frequency in the word2 and add it to dict
        for x in word2 :
            if x not in chars_in_word2:
                chars_in_word2[x] = 1
            else :
                chars_in_word2[x] = chars_in_word2[x] + 1
        
        #Loops (lines 36 to 41) to check whether both words contain the same \
        #characters
        for x in word2 :
            if x not in chars_in_word1:
                return "Not an Anagram."
        for x in word1 :
            if x not in chars_in_word2:
                return "Not an Anagram."
        
        #Loop to check the frequency equivalence of the two dicts
        for x in word1:
            if chars_in_word1[x] != chars_in_word2[x] :
                return "Not an Anagram."                
        else :
            return "Anagram it is."
    else :
        return "Not an Anagram."

#One thing, this doesn't look for meanings of the words, hence meaningless \
#can also be entered
print(anagram_check('biinary', 'braainy'))    

