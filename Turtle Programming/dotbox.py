Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle

wn = turtle.Screen()
wn.bgcolor('black')
T = turtle.Turtle()
T.color('white')
SyntaxError: multiple statements found while compiling a single statement
>>> import turtle
>>> wn = turtle.Screen()
>>> wn.bgcolor('black')
>>> T = turtle.Turtle()
>>> T.color('white')
>>> T.home = -200, 200
>>> T.home()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    T.home()
TypeError: 'tuple' object is not callable
>>> T.home
(-200, 200)
>>> T.goto(T.home)
>>> T.goto(200, 200)
>>> T.goto(T.home)
>>> T.right(90)
>>> T.forward(400)
>>> T.left(90)
>>> T.forward(400)
>>> T.left(90)
>>> T.forward(400)
>>> T.goto(-200, -200)
>>> T.goto(0, 0)
>>> T.goto(200, -200)
>>> T.width(5)
>>> T.up
<bound method TPen.penup of <turtle.Turtle object at 0x0000025070BE5780>>
>>> T.up()
>>> T.goto(-200, 0)
>>> T.right()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    T.right()
TypeError: right() missing 1 required positional argument: 'angle'
>>> T.right(90)
>>> T.forward(400)
>>> T.down()
>>> T.back(400)
>>> T.up()
>>> T.goto(T.home)
>>> for i in range(20):
	T.down()
	T.forward(400)
	T.up()
	T.back(400)
	T.right(90)
	T.forward(20)
	T.left(90)

	
>>> T.down()
>>> T.forward(400)
>>> T.up()
>>> T.goto(T.home)
>>> T.right(90)
>>> for i in range(21):
	T.down()
	T.forward(400)
	T.up()
	T.back(400)
	T.left(90)
	T.forward(20)
	T.right(90)

	
>>> T.color('red')
>>> T.up()
>>> T.goto(T.home)
>>> T.left()
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    T.left()
TypeError: left() missing 1 required positional argument: 'angle'
>>> T.left()
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    T.left()
TypeError: left() missing 1 required positional argument: 'angle'
>>> T.left(90)
>>> for i in range(21):
	for j in range(21):
		T.dot()
		T.up()
		T.forward(20)
	T.up()
	T.back(400)
	T.right(90)
	T.forward(20)
	T.left(90)

	
>>> T.up()
>>> T.goto(200, -200)
>>> T.right(180)
>>> T.forward(20)
>>> T.color('blue')
>>> for i in range(21):
	for j in range(21):
		T.dot()
		T.up()
		T.forward(20)
	T.up()
	T.back(400)
	T.right(90)
	T.forward(20)
	T.left(90)

	
>>> T.up()
>>> T.goto(-400, 0)
>>> T.goto(-650, 0)
>>> T.right(180)
>>> T.color('violet')
>>> T.color
<bound method TPen.color of <turtle.Turtle object at 0x0000025070BE5780>>
>>> help(T.color)
Help on method color in module turtle:

color(*args) method of turtle.Turtle instance
    Return or set the pencolor and fillcolor.
    
    Arguments:
    Several input formats are allowed.
    They use 0, 1, 2, or 3 arguments as follows:
    
    color()
        Return the current pencolor and the current fillcolor
        as a pair of color specification strings as are returned
        by pencolor and fillcolor.
    color(colorstring), color((r,g,b)), color(r,g,b)
        inputs as in pencolor, set both, fillcolor and pencolor,
        to the given value.
    color(colorstring1, colorstring2),
    color((r1,g1,b1), (r2,g2,b2))
        equivalent to pencolor(colorstring1) and fillcolor(colorstring2)
        and analogously, if the other input format is used.
    
    If turtleshape is a polygon, outline and interior of that polygon
    is drawn with the newly set colors.
    For mor info see: pencolor, fillcolor
    
    Example (for a Turtle instance named turtle):
    >>> turtle.color('red', 'green')
    >>> turtle.color()
    ('red', 'green')
    >>> colormode(255)
    >>> color((40, 80, 120), (160, 200, 240))
    >>> color()
    ('#285078', '#a0c8f0')

>>> T.color('indigo')
>>> T.color('violet')
>>> T.width(7)
>>> T.down()
>>> import(random)
SyntaxError: invalid syntax
>>> import random
>>> randint(1, 20)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    randint(1, 20)
NameError: name 'randint' is not defined
>>> random.randint(1, 20)
15
>>> T.dot()
>>> T.undo()
>>> while T.xcor != -465:
	T.forward(1)

	
Traceback (most recent call last):
  File "<pyshell#102>", line 2, in <module>
    T.forward(1)
  File "C:\Users\Sunny\AppData\Local\Programs\Python\Python36\lib\turtle.py", line 1637, in forward
    self._go(distance)
  File "C:\Users\Sunny\AppData\Local\Programs\Python\Python36\lib\turtle.py", line 1605, in _go
    self._goto(ende)
  File "C:\Users\Sunny\AppData\Local\Programs\Python\Python36\lib\turtle.py", line 3195, in _goto
    self._update() #count=True)
  File "C:\Users\Sunny\AppData\Local\Programs\Python\Python36\lib\turtle.py", line 2663, in _update
    screen._delay(screen._delayvalue) # TurtleScreenBase
  File "C:\Users\Sunny\AppData\Local\Programs\Python\Python36\lib\turtle.py", line 566, in _delay
    self.cv.after(delay)
  File "C:\Users\Sunny\AppData\Local\Programs\Python\Python36\lib\tkinter\__init__.py", line 744, in after
    self.tk.call('after', ms)
KeyboardInterrupt
>>> T.undo
<bound method RawTurtle.undo of <turtle.Turtle object at 0x0000025070BE5780>>
>>> T.undo()
>>> T.undo()
>>> for i in range(1000) :
	T.undo()

	
>>> for i in range(660):
	T.undo()

	
>>> for i in range(200):
	T.undo()

	
>>> T.right(180)
>>> T.color('indigo')
>>> T.goto(-465, 0)
>>> T.right(180)
>>> T.forward(185)
>>> T.color('blue')
>>> T.forward(185)
>>> T.color('green')
>>> T.forward(185)
>>> T.color('yellow')
>>> T.forward(185)
>>> T.color('orange')
>>> T.forward(185)
>>> T.color('red')
>>> T.forward(185)
>>> T.up()
>>> T.goto(-650, 200)
>>> colors = ['violet', 'indigo', 'blue', 'green', 'yellow']
>>> colors.append('orange')
>>> colors.append('red')
>>> colors
['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
>>> def something() :
	for i in range(21):
		T.down()
		for c in colors:
			T.color(c)
			T.forward(185)
		T.up()
		T.back(1300)
		T.right(90)
		T.forward(20)
		T.left(90)

		
>>> something()
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    something()
  File "<pyshell#146>", line 6, in something
    T.forward(185)
  File "C:\Users\Sunny\AppData\Local\Programs\Python\Python36\lib\turtle.py", line 1637, in forward
    self._go(distance)
  File "C:\Users\Sunny\AppData\Local\Programs\Python\Python36\lib\turtle.py", line 1605, in _go
    self._goto(ende)
  File "C:\Users\Sunny\AppData\Local\Programs\Python\Python36\lib\turtle.py", line 3195, in _goto
    self._update() #count=True)
  File "C:\Users\Sunny\AppData\Local\Programs\Python\Python36\lib\turtle.py", line 2661, in _update
    self._drawturtle()
  File "C:\Users\Sunny\AppData\Local\Programs\Python\Python36\lib\turtle.py", line 3011, in _drawturtle
    width=w, top=True)
  File "C:\Users\Sunny\AppData\Local\Programs\Python\Python36\lib\turtle.py", line 516, in _drawpoly
    self.cv.itemconfigure(polyitem, fill=fill)
  File "<string>", line 1, in itemconfigure
  File "C:\Users\Sunny\AppData\Local\Programs\Python\Python36\lib\tkinter\__init__.py", line 2578, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Users\Sunny\AppData\Local\Programs\Python\Python36\lib\tkinter\__init__.py", line 1476, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
KeyboardInterrupt
>>> T.undo()
>>> T.undo(20)
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    T.undo(20)
TypeError: undo() takes 1 positional argument but 2 were given
>>> for i in range(20):
	T.undo()

	
>>> for i in range(50):
	T.undo()

	
>>> for i in range(50):
	T.undo()

	
for i in range()
>>> for i in range(30):
	T.undo()

	
>>> def something() :
	for i in range(21):
		T.down()
		for c in colors:
			T.color(c)
			T.forward(185.7)
		T.up()
		T.back(1300)
		T.right(90)
		T.forward(20)
		T.left(90)

>>> 
>>> something()
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    something()
  File "<pyshell#162>", line 6, in something
    T.forward(185.7)
  File "C:\Users\Sunny\AppData\Local\Programs\Python\Python36\lib\turtle.py", line 1637, in forward
    self._go(distance)
  File "C:\Users\Sunny\AppData\Local\Programs\Python\Python36\lib\turtle.py", line 1605, in _go
    self._goto(ende)
  File "C:\Users\Sunny\AppData\Local\Programs\Python\Python36\lib\turtle.py", line 3179, in _goto
    self._update()
  File "C:\Users\Sunny\AppData\Local\Programs\Python\Python36\lib\turtle.py", line 2663, in _update
    screen._delay(screen._delayvalue) # TurtleScreenBase
  File "C:\Users\Sunny\AppData\Local\Programs\Python\Python36\lib\turtle.py", line 566, in _delay
    self.cv.after(delay)
  File "C:\Users\Sunny\AppData\Local\Programs\Python\Python36\lib\tkinter\__init__.py", line 744, in after
    self.tk.call('after', ms)
KeyboardInterrupt
>>> for i in range(300):
	T.undo()

	
undogoto: HALLO-DA-STIMMT-WAS-NICHT!
>>> T.up()
>>> T.goto(-650, 0)
>>> def something() :
	for i in range(1):
		T.down()
		for c in colors:
			T.color(c)
			T.forward(185.7)
		T.up()
		T.back(1300)
		T.right(90)
		T.forward(20)
		T.left(90)

>>> something()
>>> T.up()
>>> T.goto(-650, 200)
>>> something()
T
>>> T.up()
>>> T.goto(-650, -200)
>>> something()
>>> ts = turtle.getscreen()
>>> ts.getcanvas().postscript(file='dotbox.eps')
'0 348 moveto\n-9 353 lineto\n-7 348 lineto\n-9 343 lineto\n0 348 lineto\n0.000 0.000 0.000 setrgbcolor AdjustColor\neofill\n0 348 moveto\n-9 353 lineto\n-7 348 lineto\n-9 343 lineto\n0 348 lineto\n1 setlinejoin 1 setlinecap\n1 setlinewidth\n[] 0 setdash\n0.000 0.000 0.000 setrgbcolor AdjustColor\nstroke\n'
>>> 
