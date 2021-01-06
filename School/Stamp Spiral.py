import turtle as bob

bob.shape('turtle')
bob.color('blue')
bob.getscreen().bgcolor('#90EE90')

x = 20
for i in range(25):
    bob.pu()
    bob.circle(x, 30)
    bob.pd()
    bob.stamp()
    x += 5
bob.done()
