from random import *
import turtle as trl

trl.shape('turtle')
trl.speed(100)
wish = 'more'
while wish == 'more':
    for i in range(80):
        trl.left(randint(0, 360))
        trl.forward(randint(3, 45))
    wish = input()
trl.done()
