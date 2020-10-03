import turtle as trl


def circle(di):
    for i in range(90):
        trl.forward(4)
        trl.left(di * 4)


trl.shape('turtle')
trl.speed(5)
for i in range(3):
    circle(1)
    circle(-1)
    trl.left(60)
trl.done()
