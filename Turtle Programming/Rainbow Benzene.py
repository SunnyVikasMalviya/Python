import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Rainbow Benzene")
T = turtle.Turtle()

colors = ['purple', 'blue', 'green', 'yellow', 'orange', 'red']

t = turtle.Pen()

for x in range(360) :
    t.pencolor(colors[x%6])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)

