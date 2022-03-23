import turtle

x = -100
y =  100

line = " "
for i in range(1, 12):
    for j in range(1, i):
        line += str(j) + " "

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(line, font = ("맑은 고딕", 18, "bold"))

    line = " "
    y -= 20
    
turtle.hideturtle()
turtle.done()
