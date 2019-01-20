#Eval is short for evaluate
#It can only be used for evaluation of expressions and not defining
#eval() is inbuilt

list_str = "[34,56,78,23]"
list_str = eval(list_str)
print(list_str)
print(list_str[3])


x = input("type your code:")
print(x)
y = eval(input("type your code:"))

#Type print("hi"), x=5 and 5>10 while running the code
#It will do nothing in case of x
#But will evaluate it in case of y
"""
Explanation:
x is just taking in a string input. It doesn't evaluate even if you input a\
python instruction like print().
But y, y is evaluatiing the string input() and then the result is stored in y.
So y=5>10 will just store False in y but will not print. In order to print y,
you have to exclusively enter code as print(5>10)
"""
