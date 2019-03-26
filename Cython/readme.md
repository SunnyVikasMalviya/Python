For more information : https://pythonprogramming.net/introduction-and-basics-cython-tutorial/

We need two things:

Cython
A C/C++ compiler
For #1, you just simply do pip install cython For #2, things can get a little more hairy depending on your operating system:

Linux: Congratulations, you're probably done, likely already having a compiler. If not, a sudo apt-get install build-essential is likely all you need to do.

Mac: You want GCC most likely. You can do this by installing Apple's XCode

Windows: Use either MinGW, or get the exact same version of Visual C that compiled your version of Python. Here's the Cython guide for MinGW on Windows: http://cython.readthedocs.io/en/latest/src/tutorial/appendix.html You can also look into Python(x,y), Enthought Canopy, or WinPython, all of these I believe come with MinGW ready to go for you to make life easier (possibly, no promises!).

Once you have Cython and a compiler, let's go through the Cython workflow and make our own C-Exension! Let's start with a simple python file:

#example_original.py
def test(x):
    y = 0
    for i in range(x):
        y += i
    return y
How do we prepare this file to be passed through Cython? Simple, rather than .py, we do .pyx

#example_cython.pyx
def test(x):
    y = 0
    for i in range(x):
        y += i
    return y
We obviously don't have any typing information yet. We'll add that in later, but, for now, we'll stick with this.

Once you have a .pyx, you're ready to build. To do this, we're going to make a setup.py file:

from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize('example_cython.pyx'))
Next, in your terminal, do:

python setup.py build_ext --inplace

This should create a build directory, a C file (.c), and a Shared Object file (.so). With this, we can import our C-extension. To illustrate this, you can now delete, or otherwise move your example.py and example.pyx files so all that remains is the build, .c and .so files. Now create a new file called testing.py, and we can import our new c extension:

#testing.py
import example_cython

example_cython.test(5)
Congratulations! You did it!
