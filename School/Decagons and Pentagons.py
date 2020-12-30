import turtle as bob

size = 50
bob.speed(0)
bob.pensize(2)


def draw_decagon():
    for d in range(10):
        bob.fd(size)
        bob.lt(36)


def draw_pentagon():
    for p in range(5):
        bob.fd(size * 2)
        bob.lt(72)


bob.color("red")
for i in range(10):
    draw_decagon()
    bob.lt(36)
bob.setheading(0)
bob.color("blue")
for j in range(10):
    draw_pentagon()
    bob.lt(36)

bob.done()
