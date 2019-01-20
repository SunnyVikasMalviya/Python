#PICKLIING aka Flattning, Serialization, Marshalling
#Pickle module is used for converting python objects into byte stream
#Anything that requires a lot of processing and ends in an object can be made\
#faster using pickling
#eg: loading a machine learning dataset, Data from json or sql etc.
#Pickle module is inbuilt in python
import pickle

example_dict = {1:'4', 2:'5', 3:'6'}

pickle_out = open("dict.pickle","wb")
pickle.dump(example_dict, pickle_out)
pickle_out.close()
