from playsound import playsound
playsound(r'C:\Users\Sunny\Music\english\I.mp3')



"""
The code below will not work, because we are providing a normal string as our\
path name.

playsound('C:\Users\Sunny\Music\english\I.mp3')

In order to solve this problem, we can do the following:
1. Place 'r' before the pathname.
    The r converts the normal string pathname to raw pathname
    playsound(r'C:\Users\Sunny\Music\english\I.mp3')
2. Change the backward slash(s) to forward slash(s).
    playsound('C:/Users/Sunny/Music/english/I.mp3')
3. Use 2 concurrent backward slash(s).
    playsound('C:\\Users\\Sunny\\Music\\english\\I.mp3')

"""
