# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 18:09:02 2018

@author: Sunny
"""
"""Used for interacting with Cmd Line"""
import sys
#sys is a standard library package for python which doesn't need explicitly \ 
#downloding but it needs importing

#No effective difference between stderr and stdout
sys.stderr.write("Error\n")
sys.stderr.flush()
sys.stdout.write("Output\n")

print(sys.argv)

#sys.argv contains the path of the file 
#sys.argv is a list of arguments that the cmd line takes from the python
#This conditional stmt just checks if the number of elements in the list is \
#more than 1 than it prints the second argument and adds 5 to the third \
#integral argument
if len(sys.argv) > 1:
    print(sys.argv[1])
    print(float(sys.argv[2])+5)

'''What to do to make the above code work'''
#After writing all this code, save it to a folder. Press shift and right-click\
#on the folder to open the extended selection dropdown menu. Click on the \
#Open with Windows Power Shell or Cmd Prompt.
#In Shell, type "py sys_module.py, 'Argument 1', 5.67" and hit enter
