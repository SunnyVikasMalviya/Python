# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 19:05:32 2018

@author: Sunny
"""


def string_rotation(word1, word2) :
    #Taking 2 words as input parameters
    #If lengths aren't equal, straight away deny rotations of each other
    if len(word1) == len(word2) :
        #Loop to rotate the word2 from an index from 0 through length of the word  
        for x in range(len(word1)) :
            #A word that contains the rotated_word2 by slicing it from the index
            rotated_word2 = word2[x:] + word2[:x]
            if word1 == rotated_word2 :
                return "Rotations of each other"
        else :
            return "Not rotations of each other"
    else :
        return "Words are totally different, they don't even have the same length"
    
#print(string_rotation("Hello World", "lo WorldHel"))      #For Debugging