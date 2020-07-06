import turtle

a = input("on or off")

turtle.pencolor('yellow')
turtle.pensize(4)
turtle.fillcolor('green')
turtle.begin_fill()
turtle.goto(40,0)
turtle.goto(40,20)
turtle.goto(0,20)
turtle.goto(0,0)
turtle.end_fill()

turtle.penup()
turtle.goto(40,10)
turtle.down()
turtle.fd(100)
turtle.goto(140,100)
turtle.goto(40,100)
turtle.penup()
turtle.goto(20,80)
turtle.pendown()

turtle.fillcolor('b')
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

turtle.penup()
turtle.goto(0,100)
turtle.pendown()
turtle.bk(100)
turtle.goto(-100,10)
turtle.goto(0,10)

if a =  (这里不知道怎么搞，输了好多次都不知道怎么改)
    b= 'red'
else:
    b = 'black'



turtle.done()