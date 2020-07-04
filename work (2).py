import turtle
import time
turtle.hideturtle()
for i in range(5):
    turtle.speed(20)
    turtle.fillcolor('red')
    turtle.penup()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    time.sleep(2)

    turtle.fillcolor('white')
    turtle.penup()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

    turtle.fillcolor('yellow')
    turtle.penup()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

    turtle.fillcolor('white')
    turtle.penup()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

turtle.done()


