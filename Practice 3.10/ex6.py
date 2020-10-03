import turtle as trl

trl.shape('turtle')
n = 12
n = int(input())
for i in range(n):
    trl.forward(200)
    trl.stamp()
    trl.backward(200)
    trl.left(360/n)
trl.done()
