import urllib2          #just urllib

try:
    x = urllib2.urlopen("http://pythonprogramming.net").read()    #just urllib
    print x            #pirnt(x)
except Exception, e:           #except Exception as e:
    print str(e)         #print(str(e))


"""
The above code is written in python 2.x.
In order to change it to 3.x, we use the 2to3.py module.
After creating a file in 2.x, just type the below command in command prompt.
Make sure the file trying2to3.py is in the current working directory.
We are going to pass our 2.x file named trying2to3.py as an argument to the 2to3.py module from the command line interface.

py C:\Users\Sunny\AppData\Local\Programs\Python\Python37-32\Tools\scripts\2to3.py trying2to3.py

The above command just displays the errors and the corrections that we need to make in the file.
But it doesn't actually correct the original file.
In order to correct the original file, just add '-w' after the path of the 2to3.py module.

py C:\Users\Sunny\AppData\Local\Programs\Python\Python37-32\Tools\scripts\2to3.py -w trying2to3.py

The modified file is the original one and a backup of the original file is kept.
"""
