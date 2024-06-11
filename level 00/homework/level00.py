from turtle import*

#we need to pain a house :D
width(5)
color("blue")
begin_fill()
forward(200)

#step one draw a square 

left(90)

forward(200)

left(90)

forward(200)
left(90)

forward(200)




end_fill()


left(90)

forward(70)
color("yellow")
begin_fill()

left(90)

forward(70)
right(90)

forward(50)

right(90)
forward(70)

right(90)
forward(50)
end_fill()

penup()
goto(200, 200)
pendown()
color("red")
begin_fill()

right(40)
forward(125)

left(77)
forward(131)
left(143)
forward(200)
end_fill()

penup()

goto(0, 0)
pendown()
color("green")
begin_fill()
forward(500)
right(90)
forward(100)
right(90)
forward(700)
right(90)
forward(100)
right(90)
forward(200)
end_fill()
exitonclick()