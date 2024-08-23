import turtle

a = turtle.Turtle()
a.shape('turtle')
a.pencolor('blue')
a.width(2)

i = 0
n = 300
while i < 6:
    a.forward(n)
    a.left(90)
    
    a.forward(n)
    a.left(90)

    a.forward(n)
    a.left(90)

    a.forward(n)
    a.left(90)

    a.up()
    a.forward(25)
    a.left(90)
    a.forward(25)
    a.right(90)
    a.down()

    n -= 50
    i += 1

radius = 70
a.up()
a.right(90)
a.forward(radius)
a.left(90)
a.down()

a.fillcolor('green')
a.begin_fill()
a.circle(radius)
a.end_fill()

turtle.exitonclick()
