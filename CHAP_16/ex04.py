import turtle

t=turtle.Pen()
t.speed(10)

def mystar(size, filled):
    if filled:
        t.begin_fill()

    for x in range(1,10):
        t.forward(size)
        t.left(175)
        t.forward(size)
        t.left(225)

    if filled:
        t.end_fill()

t.color(0.9,0.75,0)
mystar(120, True)

t.color(0,0,0)
mystar(120, False)

turtle.done()