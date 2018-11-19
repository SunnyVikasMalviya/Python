# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 17:41:43 2018

@author: Sunny
"""

import urllib.request

x = urllib.request.urlopen("https://www.google.com/")
print(x.read())