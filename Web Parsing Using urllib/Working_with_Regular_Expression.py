import re

Data = '''
Vikas is 20 years old, and Ajay is 43 years old.
Edward is 37 years old, and his grandfather, Dan, is 102.
'''

ages = re.findall(r'\d{1,3}', Data)
names = re.findall(r'[A-Z][a-z]*', Data)
'''
What happens here is:
1. findall() is a function in the re library to parse through i.e. go through the \
   whole data and find all the instances of the given re 
2. r'' is used to denote that the stuff in the parenthesis is a regular expression
3. \d is used to represent a digit
4. {1,3} is used to represent that their can be 1, 2 or 3 digits
5. [A-Z] is used to denote that the first Character is a Capital letter
6. [a-z] is used to denote that the letter is a small letter
7. * is used to denote 0 or more and in this case [a-z]* denote their can be 0 or \
   more small letters
'''

#print(ages)
#print(names)

#Below we are just storing the data into a dictionary
dataDict = {}

x = 0
for each_name in names :
    dataDict[each_name] = ages[x]
    x+=1

print(dataDict)
