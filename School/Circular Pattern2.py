import turtle as bob

bob.speed(0)
radius = 5

for i in range(20):
    bob.circle(radius)
    bob.circle(-radius)
    bob.lt(10)
    radius += 8


print()
bob.done()
