import turtle as trtl     

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
#draw branch
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
painter.goto(350,-350)
painter.pendown()
painter.pensize(15)
petals = 0
while (petals < 18):
  painter.right(20)
  painter.forward(30)
  painter.stamp()
  petals = petals + 1

painter.color('light green')
#second trunk
painter.penup()

painter.goto(250, -350)
painter.pendown()
painter.setheading(90)
painter.forward(100)
#draw branch
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

painter.penup()
#third trunk
painter.goto(-250, -350)
painter.pendown()
painter.setheading(90)
painter.forward(100)
#draw branch
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






wn = trtl.Screen()
wn.mainloop()