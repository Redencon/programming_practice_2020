import turtle as trl


def star(n):
    for i in range(n):
        trl.forward(150)
        trl.left(180 - (360 / 2 / n))


trl.shape('turtle')
star(5)
trl.penup()
trl.goto(-250, 0)
trl.pendown()
star(11)
trl.done()
