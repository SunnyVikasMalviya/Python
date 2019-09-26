import turtle

wn = turtle.Screen()
wn.bgcolor("orange")
wn.title("Spiral Helix")
T = turtle.Turtle()

for i in range(10) :
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)

