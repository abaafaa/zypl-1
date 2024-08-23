import turtle

a = turtle.Turtle()
a.shape('turtle')
a.width(2)
i = 0
n = 300

while i < 6:
    for _ in range(4):
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
