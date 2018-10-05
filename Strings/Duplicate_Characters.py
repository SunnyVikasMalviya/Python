# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 20:07:08 2018

@author: Sunny
"""

#The function below takes a string and returns the duplicate characters in the \
#string 
#Capital and Small characters are treated as different
def find_dup_chars(word) :
    #List that stores the characters in the string
    list_=[]
    #list that stores the characters appearing more than once
    list_dup=[]
    for x in word :
        if x not in list_:
            list_.append(x)
        else :
            list_dup.append(x)
    return list_dup

print(find_dup_chars('Jjjethetis'))