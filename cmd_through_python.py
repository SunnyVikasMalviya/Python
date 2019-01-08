'''
So till now we have been opening the scripts with mouse clicks. We learned in \
system module tutorial how to communicate from the shell to the python files.
Here we will learn how to communicate from the python script to the shell.
Subprocess module is used for the exact same function. Also by using this we \
communicate between different python scripts since through shell we can access\
python scripts and now we can access shell through python script.
'''



import subprocess


output = subprocess.check_output('dir', shell=True)
#Here we run dir command through python in the shell
with open("Py_to_shell.txt", "w") as file :
    file.write(str(output))
    
#print(output)          #For Debugging


#we can also use the below line if we just want to run commands without needing\
#output returned to us. The subprocess runs in the background.
#subprocess.call('dir', shell=True)
