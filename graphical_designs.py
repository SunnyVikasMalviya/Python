# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 19:47:10 2018

@author: Sunny
"""

#Graphical Design

#from terminal import render
class designs:
    yellow = '\033[93m'
    bold = '\033[1m'
    underline = '\033[4m'
    end = '\033[0m'
    red = '\033[31m'
    green = '\033[32m'
    italics = '\033[3m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    darkcyan = '\033[36m'
    grey = '\033[37m'
    
    
    
print (designs.bold + "Hello World!!!" + designs.end)
print (designs.purple + "Hello World!!!" + designs.end)
#print (designs.cyan + "Hello World!!!" + designs.end)
print (designs.darkcyan + "Hello World!!!" + designs.end)
print (designs.blue + "Hello World!!!" + designs.end)
print (designs.green + "Hello World!!!" + designs.end)
print (designs.yellow + "Hello World!!!" + designs.end)
print (designs.red + "Hello World!!!" + designs.end)
print (designs.underline + "Hello World!!!\n\n" + designs.end)
#print.render('%(BG_YELLOW)s%(RED)s%(BOLD)sHello World!!!%(NORMAL)s')
#print (designs. + "Hello World!!!" + designs.end)
