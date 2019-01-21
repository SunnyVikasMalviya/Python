#exec() compiles and evaluates whatever you pass through it.
#NO SECURITY
#its a compiler in compiler

exec("print('so this works')")

list_str = "[4,5657,3,43345,234]"
list_str = exec(list_str)
print(list_str)


exec("list_str2 = [423,235,567]")
print(list_str2)

exec("def test(): print('Oh snip snap if this works')")
exec("test()")

exec("""
def test1():
    print('See whether multiline works.')

test1()
"""
   )




