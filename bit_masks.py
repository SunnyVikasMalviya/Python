#bit masks
#1. To check whether the 4th bit is on or not
def check_bit4(input):
  mask = 0b1000
  if input & mask > 0:
    return "on"
  else :
    return "off"
	
#2. To turn on the third bit 
a = 0b10111011
mask = 0b100
print bin(a | mask)

#3. To flip all the eight bits
a = 0b11101110
mask = 0b11111111
print bin(a ^ mask)

#4. To flip the desired bit in a given number
def flip_bit(number, n):
  mask = 0b1 << (n-1)
  result = number ^ mask
  return bin(result)