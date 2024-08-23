import turtle
import math as M

a = turtle.Turtle()
a.shape('turtle')
a.width(2)

i = 0
n = 300
h = 0

while i < 4:
    a.forward(n - h)
    a.left(90)
    a.forward(n - h)
    a.left(135)
    a.forward(M.sqrt(2 * pow(n - h, 2)))
    a.left(135)

    a.up()
    a.forward(25)
    a.left(90)
    a.forward(25)
    a.right(90)
    a.forward(25)
    a.down()

    n -= 50
    i += 1
    h += 25
