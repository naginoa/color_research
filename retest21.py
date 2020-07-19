import turtle
lst = ['red','orange','yellow','green','skyblue','blue','purple']
size = 20
pos_x = 0
r = 100
for i in range(len(lst)):
    turtle.goto(r, 0)
    turtle.pendown()
    turtle.pencolor(lst[-i])
    turtle.pensize(size)
    turtle.left(90)
    turtle.circle(r, 180)
    turtle.penup()
    turtle.left(90)
    size -= 2
    pos_x -= 9
    r -= 9
    turtle.hideturtle()

turtle.done()
