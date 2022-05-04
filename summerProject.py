import turtle as trtl     

painter = trtl.Turtle()
painter.speed(0)

#Trunks of trees
painter.color("brown")
painter.pensize(60)
painter.penup()
painter.goto(0, -350)
painter.pendown()
painter.setheading(90)
painter.forward(200)
painter.pensize(30)
painter.setheading(135)
painter.forward(100)
painter.forward(200)

painter.penup()

painter.goto(250, -350)
painter.pendown()
painter.setheading(90)
painter.forward(400)

painter.penup()

painter.goto(-250, -350)
painter.pendown()
painter.setheading(90)
painter.forward(400)






wn = trtl.Screen()
wn.mainloop()