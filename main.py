import turtle
screen = turtle.Screen()
screen.screensize(canvwidth= 500, canvheight= 500)
screen.bgcolor('tan')
t = turtle.Turtle()
t.speed(0)
t. penup()

t.pencolor("blue")
t.goto(-80,15)
t.pendown()
t.circle(35)

t. penup()
t.pencolor("black")
t.goto(0,15)
t.pendown()
t.circle(35)

t. penup()
t.pencolor("red")
t.goto(80,15)
t.pendown()
t.circle(35)

t. penup()
t.pencolor("yellow")
t.goto(-40,-20)
t.pendown()
t.circle(35)

t. penup()
t.pencolor("green")
t.goto(40,-20)
t.pendown()
t.circle(35)


t.penup()
t.goto (0,100)
t.pencolor("purple")
t.write("Winter Olympics",font=("Arial",30,"bold italic"),align="center")

t.penup()
t.goto (0,-100)
t.pencolor("purple")
t.write("2026",font=("Arial",30,"bold italic"),align="center")


turtle.done()