import turtle as trl

trl.shape('turtle')
for i in range(10):
    for j in range(4):
        trl.forward(5*(2*i + 1))
        trl.left(90)
    trl.left(180)
    trl.penup()
    trl.forward(5)
    trl.left(90)
    trl.forward(5)
    trl.left(90)
    trl.pendown()
trl.done()
