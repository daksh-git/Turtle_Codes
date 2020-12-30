import turtle

bob = turtle.Turtle()
bob.speed(10)

i = 1

bob.color("#774936", "#edc4b3")
bob.begin_fill()
while i <=36:
    bob.fd(200)
    bob.lt(170)
    i += 1

bob.end_fill()

turtle.done()
