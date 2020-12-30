import turtle as bob

bob.pensize(15)

bob.pu()
bob.goto(-100, 0)
bob.pd()

colors = ["blue", "black", "red"]
for i in colors:
    bob.color(i)
    bob.circle(100)
    bob.pu()
    bob.forward(240)
    bob.pd()

bob.pu()
bob.goto(260, -100)
bob.pd()


colors_2 = ["green", "yellow"]
for a in colors_2:
    bob.color(a)
    bob.circle(100)
    bob.pu()
    bob.backward(240)
    bob.pd()

bob.done()
