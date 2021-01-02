import turtle as bob

bob.speed(0)

screen = bob.getscreen()
screen.bgcolor("Black")
bob.color('cyan')

side = 30

for a in range(300):
    bob.fd(side)
    bob.rt(91)
    side += 1
bob.done()
