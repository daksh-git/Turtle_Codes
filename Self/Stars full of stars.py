import turtle

bob = turtle.Turtle()
screen = bob.getscreen()
screen.bgcolor("#994444")
bob.penup()
bob.goto(-200, 100)
bob.pendown()

bob.speed(0)


def star(turtle, size):
    if size <= 10:
        return
    else:
        turtle.begin_fill()
        for i in range(5):
            turtle.fd(size)
            star(turtle, size / 3)
            turtle.lt(216)
        turtle.end_fill()


star(bob, 300)

turtle.done()
