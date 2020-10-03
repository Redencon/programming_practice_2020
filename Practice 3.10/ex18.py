from random import randint
import turtle


number_of_turtles = 10
steps_of_time_number = 1000
border_size = 150
turtle_size = 350

turtle.penup()
turtle.goto(-border_size, -border_size)
turtle.color('red')
turtle.pendown()
turtle.goto(-border_size, border_size)
turtle.goto(border_size, border_size)
turtle.goto(border_size, -border_size)
turtle.goto(-border_size, -border_size)

pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-border_size, border_size), randint(-border_size, border_size))
    #unit.goto(0, 0)
    unit.setheading(randint(0, 360))


for i in range(steps_of_time_number):
    for unit in pool:
        unit.forward(2)
        x, y = unit.pos()
        if x < -border_size:
            unit.setheading(randint(-90, 90))
        if x > border_size:
            unit.setheading(randint(90, 270))
        if y < -border_size:
            unit.setheading(randint(0, 180))
        if y > border_size:
            unit.setheading(randint(180, 360))
        for units in pool:
            if unit != units:
                i, j = units.pos()
                dist = (i - x)*(i - x) + (j - y)*(j - y)
                if dist < turtle_size:
                    if j < y:
                        unit.setheading(randint(0, 180))
                        units.setheading(randint(180, 360))
                    if j > y:
                        units.setheading(randint(0, 180))
                        unit.setheading(randint(180, 360))
turtle.done()
