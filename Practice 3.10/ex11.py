import turtle as trl


def circle(direction, speed):
    for i in range(90):
        trl.forward(speed*2)
        trl.left(direction*4)


trl.shape('turtle')
trl.right(90)
for i in range(50, 100, 10):
    circle(1, i/50)
    circle(-1, i/50)
trl.done()

