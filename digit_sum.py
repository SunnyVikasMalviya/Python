#sum of digits
def digit_sum(n):
  n = list(str(n))
  res = 0
  for x in n:
    res += int(x)
  return res
print digit_sum(1234)

#is integer
def is_int(x):
  if abs(x) - int(abs(x)) > 0:
    return False
  else  :
    return True
	
#factorial
def factorial(x):
  fact = 1
  for n in range(1, x+1):
    fact *= n
  return fact
  
#is prime
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True

#reverse listdef reverse(text):
    word = ""
    l = len(text) - 1
    while l >= 0:
        word = word + text[l]
        l -= 1
    return word
	
#removing vowels
def anti_vowel(text):
  word = ""
  for x in text:
    if x not in ('a','e','i','o','u','A','E','I','O','U'):
      word += x      
  return word
  
#item occurence in a list
def count(sequence, item):
item_occurence = 0
	for x in sequence:
		if item == x:
			item_occurence += 1
	return item_occurence
   
#removing odd numbers from a list
def purify(numbers):
  copy_of_numbers = []
  for x in numbers:
    if x % 2 == 0:
      copy_of_numbers.append(x)
  return copy_of_numbers
  
#product of numbers present in a list
def product(numbers):
  product = 1
  for x in numbers:
    product *= x
  return product
  
#removing duplicate elements from a list
def remove_duplicates(original_list):
  new_list = []
  for x in original_list:
    if x not in new_list:
      new_list.append(x)
  return new_list
  
#getting median of a given unsorted list of elements
def median(lst):
    sorted_list = sorted(lst)
    if len(sorted_list) % 2 != 0:
        #odd number of elements
        index = len(sorted_list)//2 
        return sorted_list[index]
    elif len(sorted_list) % 2 == 0:
        #even no. of elements
        index_1 = len(sorted_list)/2 - 1
        index_2 = len(sorted_list)/2
        mean = (sorted_list[index_1] + sorted_list[index_2])/2.0
        return mean
   