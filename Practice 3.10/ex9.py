import turtle as trl
import numpy as np

trl.shape('turtle')


def poly(r, n):
    a = r * 2 * np.sin(np.pi / n)
    trl.left(90 + (360 / (n * 2)))
    for i in range(n):
        trl.forward(a)
        trl.left(360 / n)
    trl.right(90 + (360 / (n * 2)))


rad = 0
for j in range(3, 15):
    trl.penup()
    trl.forward(15)
    trl.pendown()
    rad += 15
    poly(rad, j)
trl.done()
