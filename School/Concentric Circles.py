import turtle as bob

initial_radius = 140
bob.speed(0)
bob.pu()
bob.goto(0, -100)
bob.pd()
bob.pensize(2)

colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]


for i in colors:
    bob.color("black", i)
    bob.begin_fill()
    bob.circle(initial_radius)
    bob.end_fill()
    bob.pu()
    bob.lt(90)
    bob.fd(20)
    bob.setheading(0)
    bob.pd()
    initial_radius -= 20

bob.done()
