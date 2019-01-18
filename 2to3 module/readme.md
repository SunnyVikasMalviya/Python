The 2to3.py module helps us convert the python code written in python 2.x to python 3.x.
Step 1: Write a script in python 2.x.  say example.py
Step 2: Open command prompt and cd to the parent directory of the example.py.
Step 3: For just knowing the modifications needed, type the below command:
      Syntax: py path_of_2to3.py_module example.py
      Example: py C:\Users\Sunny\AppData\Local\Programs\Python\Python37-32\Tools\scripts\2to3.py trying2to3_corrected.py
Step 4: For making modifications in the original file and saving a example.bak backup file, type the below command:
      Syntax: py path_of_2to3.py_module -w example.py
      Example: py C:\Users\Sunny\AppData\Local\Programs\Python\Python37-32\Tools\scripts\2to3.py -w trying2to3_corrected.py
Step 5: The script conversion is done. You may now run your script.
