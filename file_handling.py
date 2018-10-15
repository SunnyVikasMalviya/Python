#To write a list in a file
my_list = [i ** 2 for i in range(1, 11)]
# Generates a list of squares of the numbers 1 - 10
f = open("output.txt", "w")
for item in my_list:
  f.write(str(item) + "\n")
f.close()



#To read from the file
my_file = open("output.txt", "r")
print (my_file.read())
my_file.close()



#To read individual lines from the file
my_file = open("text.txt", "r")
print (my_file.readline())
print (my_file.readline())
print (my_file.readline())
my_file.close()



#To simultaneously write and from the file
# Use a file handler to open a file for writing
write_file = open("text.txt", "w")
# Open the file for reading
read_file = open("text.txt", "r")
# Write to the file
write_file.write("Not closing files is VERY BAD.")
write_file.close()
# Try to read from the file
print (read_file.read())
read_file.close()



#To write to a file using 'with' and 'as' that automatically closes the file; also closed is used to check whether the file has been closed or not
with open("text.txt", "w") as my_file:
  my_file.write("Hi There")
  
if not my_file.closed:
  my_file.close()
  
print (my_file.closed)