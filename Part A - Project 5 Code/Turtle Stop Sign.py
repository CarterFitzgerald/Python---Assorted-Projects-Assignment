import turtle

turtle.hideturtle()
turtle.pencolor('red')
turtle.fillcolor("red")
turtle.begin_fill()

i = 6
while i > 0:
    turtle.forward(100)
    turtle.lt(60)
    i -= 1
turtle.end_fill()
turtle.lt(90)
turtle.forward(60)
turtle.lt(90)
turtle.forward(5)

turtle.pencolor('white')
turtle.write("STOP", font=("Times new roman", 35, "normal"))

turtle.done()
