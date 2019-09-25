import turtle

wn = turtle.Screen()
wn.bgcolor("light blue")
wn.title("Triangle")
T = turtle.Turtle()
T.color("white")
def sqrfunc(size) :
    for i in range(28) :
        T.fd(size)
        T.left(90)
        size = size - 5

sqrfunc(146)
#sqrfunc(126)
#sqrfunc(106)
#sqrfunc(86)
#sqrfunc(66)
#sqrfunc(46)
#sqrfunc(26)
#sqrfunc(6)
