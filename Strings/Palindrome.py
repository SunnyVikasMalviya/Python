# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 19:01:09 2018

@author: Sunny
"""
from Rev_Word_Using_Recrr import rev_rec

def palindrome(word) :
    if word == rev_rec(word) :
        return "Palindrome"
    else :
        return "Not a palindrome"
    
#print(palindrome("HelleH"))    #For Debugging