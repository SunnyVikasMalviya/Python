import turtle
import random

def snowflakes(size) :
    elsa.penup()
    elsa.forward(10*size)
    elsa.left(45)
    elsa.pendown()
    elsa.color(random.choice(sfcolor))
    for i in range(8) :
        branch(size)
        elsa.left(45)

def branch(size) :
    for i in range(3) :
        for i in range(3) :
            elsa.forward(10.0*size/3)
            elsa.backward(10.0*size/3)
            elsa.right(45)
        elsa.left(90)
        elsa.backward(10.0*size/3)
        elsa.left(45)
    elsa.right(90)
    elsa.forward(10.0*size)

if __name__ == '__main__' :
    wn = turtle.Screen()
    wn.bgcolor('cyan')

    elsa = turtle.Turtle()
    elsa.speed(20)

    sfcolor = ['white', 'grey', 'blue', 'pink', 'red', 'yellow', 'green']

    for i in range(20):
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        sf_size=random.randint(1,4)
        elsa.penup()
        elsa.goto(x,y)
        elsa.pendown()
        snowflakes(sf_size)
    wn.exitonclick()
