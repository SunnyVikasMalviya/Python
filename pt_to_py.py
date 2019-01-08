import subprocess

subprocess.call('cd C:\MvikBack\Python\ToUpload\New', shell = True)
output = subprocess.check_output('py censor_words.py, "Fuck the God", "Fuck"', shell=True)
print(output)
