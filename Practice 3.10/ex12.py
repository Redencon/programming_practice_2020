import turtle as trl


def semicircle(speed):
    for i in range(90):
        trl.forward(speed)
        trl.right(2)


trl.shape('turtle')
trl.penup()
trl.goto(-300, 0)
trl.pendown()
trl.left(90)
for j in range(7):
    semicircle(1)
    semicircle(0.2)
trl.done()
