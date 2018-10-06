# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 14:37:40 2018

@author: Sunny
"""

#Function to reverse a string using recursion
def rev_rec(word):
    if len(word)==1 :
        return word
    else :
        return word[len(word)-1] + rev_rec(word[0:len(word)-1])


#print(rev_rec('Arguments Globe'))  #For Debuggimg