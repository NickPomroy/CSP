import turtle as trtl   
#Background
wn = trtl.Screen()  
wn.bgcolor('tan')

#Create Turtle
painter = trtl.Turtle()
painter.speed(0)

#Trunks of cacti
painter.color("light green")
painter.pensize(60)
painter.penup()
painter.goto(0, -350)
painter.pendown()
painter.setheading(90)
painter.forward(100)
#draw branches
painter.pensize(45)
painter.setheading(45)
painter.forward(175)

painter.penup()
painter.goto(0, -150)
painter.pendown()

painter.pensize(45)
painter.setheading(135)
painter.forward(175)

painter.penup()
painter.goto(0, -75)
painter.pendown()

painter.pensize(45)
painter.setheading(45)
painter.forward(175)

painter.penup()
painter.goto(0, -325)
painter.pendown()

painter.pensize(45)
painter.setheading(135)
painter.forward(175)

painter.penup()
painter.goto(0, -250)

painter.pendown()
painter.pensize(60)
painter.setheading(90)
painter.forward(300)

#draw flower 
painter.penup()
painter.color("darkorchid")
painter.goto(-75,95)
painter.pendown()
painter.pensize(60)
painter.shape("circle")
petals = 0
while (petals < 18):
  painter.right(30)
  painter.forward(40)
  painter.stamp()
  petals = petals + 1
painter.pensize(60)
painter.color('light green')
#second trunk
painter.penup()

painter.goto(250, -350)
painter.pendown()
painter.setheading(90)
painter.forward(100)
#draw branches
painter.pensize(45)
painter.setheading(45)
painter.forward(150)

painter.penup()
painter.goto(250, -150)
painter.pendown()

painter.pensize(45)
painter.setheading(135)
painter.forward(175)

painter.penup()
painter.goto(250, -75)
painter.pendown()

painter.pensize(45)
painter.setheading(45)
painter.forward(175)

painter.penup()
painter.goto(250, -325)
painter.pendown()

painter.pensize(45)
painter.setheading(135)
painter.forward(175)

painter.penup()
painter.goto(250, -250)


painter.pendown()
painter.pensize(60)
painter.setheading(90)
painter.forward(300)

#draw flower 
painter.penup()
painter.color("darkorchid")
painter.goto(175,95)
painter.pendown()
painter.pensize(60)
painter.shape("circle")
petals = 0
while (petals < 18):
  painter.right(30)
  painter.forward(40)
  painter.stamp()
  petals = petals + 1
painter.pensize(60)
painter.color('light green')

painter.penup()
#third trunk
painter.goto(-250, -350)
painter.pendown()
painter.setheading(90)
painter.forward(100)
#draw branches
painter.pensize(45)
painter.setheading(45)
painter.forward(150)

painter.penup()
painter.goto(-250, -150)
painter.pendown()

painter.pensize(45)
painter.setheading(135)
painter.forward(175)

painter.penup()
painter.goto(-250, -75)
painter.pendown()

painter.pensize(45)
painter.setheading(45)
painter.forward(175)

painter.penup()
painter.goto(-250, -325)
painter.pendown()

painter.pensize(45)
painter.setheading(135)
painter.forward(175)



painter.penup()
painter.goto(-250, -250)
painter.pendown()
painter.pensize(60)
painter.setheading(90)
painter.forward(300)

#draw flower 
painter.penup()
painter.color("darkorchid")
painter.goto(-325,95)
painter.pendown()
painter.pensize(60)
painter.shape("circle")
petals = 0
while (petals < 18):
  painter.right(30)
  painter.forward(40)
  painter.stamp()
  petals = petals + 1

painter.penup()
painter.turtlesize(5)
painter.goto(-250, 75)
painter.color("RED")
painter.stamp()

painter.goto(250, 75)
painter.stamp()

painter.goto(0, 75)
painter.stamp()

painter.pensize(15)
painter.turtlesize(2)
painter.color('yellow')
#sun

# define function
# for drawing rays of Sun
def drawFourRays(t, length, radius):
	
	for i in range(4):
		t.penup()
		t.forward(radius)
		t.pendown()
		t.forward(length)
		t.penup()
		t.backward(length + radius)
		t.left(90)


# Draw circle
# to make sun
painter.penup()
painter.goto(115, 250)
painter.fillcolor("yellow")
painter.pendown()
painter.begin_fill()
painter.circle(35)
painter.end_fill()

# Use the defined
# function to draw rays
painter.penup()
painter.goto(150, 250)
painter.pendown()
drawFourRays(painter, 85, 54)
painter.right(45)
drawFourRays(painter, 85, 54)
painter.left(45)

#draw ladybug
painter.turtlesize(6)
painter.penup()
painter.goto(-150, 250)
painter.color('red')
painter.stamp()
painter.turtlesize(1)
painter.color('black')
painter.goto(-130, 270)
painter.stamp()
painter.goto(-160, 260)
painter.stamp()
painter.goto(-170, 230)
painter.stamp()
painter.goto(-110, 220)
painter.stamp()
painter.goto(-150, 240)
painter.stamp()
painter.goto(-180, 270)
painter.stamp()

wn.mainloop()