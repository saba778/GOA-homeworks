from turtle import*

#we want to paint a house
#we need a square
shape("turtle")
speed(5)
width(7)
color("purple")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
#we need a door
begin_fill()
forward(70)
color("yellow")
left(90)
forward(90) #hight of the door
right(90)
forward(60)
right(90)
forward(90)
left(90)
end_fill()
color("purple")
#end door
forward(70)
left(90)
forward(200)
#end square
#we need a roof
color("black")
begin_fill()
penup()
goto(200,200)
pendown()
left(40)
forward(150)
left(98)
forward(153)
end_fill()
#we need to make windows
penup()
goto(20,100)
pendown()
begin_fill()
left(223)
forward(50)
right(90)
forward(40)
right(90)
forward(50)
right(90)
forward(40)
end_fill()
#second window
penup()
goto(140,100)
pendown()
begin_fill()
right(90)
forward(50)
right(90)
forward(40)
right(90)
forward(50)
right(90)
forward(40)
end_fill()
exitonclick()