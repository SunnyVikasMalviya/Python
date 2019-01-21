"""
Consider a number system consisting of only 4's and 7's i.e. 4, 7, 44, 47, 74, 77, 444, 447... . 
Given a number X of the number system write a program to find the position of the number in the number system. 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 14:51:11 2018
@author: Sunny
"""

#This list will contain the numbers in the number system till the entered number X.
number_system_47 = []

#Taking input of X
X = int(input("Enter a number in the number system of 4 and 7:"))
#str_X = str(X)
#print(X)
#Inserting elements into the list from 4 till X. 
for num in range(4, X+1):
    #The lines 13 to 17 checks whether a number num in range 4 to X contains only 4 and 7 as it's digits
    #It checks by converting each number to a string and checking each element of this string is either 4 or 7.
    #If all digits are 4's and 7's, then it will be appended else it will be iterate and jump to the next number.
    num1 = num
    str_num = str(num)
    for y in str_num:
        if y!='4' and  y!='7':
            break
    else :
        number_system_47.append(num1)

#So now that we have this list of number in the 4-7 number system, the index+1 of X is our required answer 
print(number_system_47)
print(number_system_47.index(X)+1)
