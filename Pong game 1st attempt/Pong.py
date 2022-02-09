import turtle as trtl
wn = trtl.Screen()

# pong ball and walls
pong = trtl.Turtle()
pong.up()
pong.shape('circle')
pong.color('white')
pong.shapesize(float(.5))
wall2 = trtl.Turtle()

wall2.up()
wall2.shape('square')
wall2.color('white')
wall2.shapesize(.5, 10, .5)
wall2.goto(-350, 0)
wall2.seth(90)

wall1 = trtl.Turtle()
wall1.up()
wall1.shape('square')
wall1.color('white')
wall1.shapesize(.5, 10, .5)
wall1.goto(350, 0)
wall1.seth(90)

wall1.hideturtle()
pong.hideturtle()
wall2.hideturtle()

angle = 0

# move buttons
def up():
    wall1.fd(10)
def LL():
    wall2.fd(10)
def Ln():
    wall2.bk(10)
def dn():
    wall1.bk(10)

# start button
strtbttn = "StartButton.gif"
wn.addshape(strtbttn)
startbutton = trtl.Turtle(shape=strtbttn)
startbutton.shapesize(1)
startbutton.color('white')
def stort():
    startbutton.ht()
    wall1.st()
    wall2.st()
    pong.st()

#while (True):
#    if (abs(pong.xcor() - wall1.xcor()) < 20):
#        if (abs(pong.ycor() - wall1.ycor()) < 20):
#            pong.seth(angle + 180)

wn.listen()
wn.bgcolor('black')
wn.onkeypress(up,"Up")
wn.onkeypress(dn, "Down")
wn.onkey(LL,"w")
wn.onkey(Ln,"s") 
wn.onkeypress(stort, "space")
wn.listen()
wn.mainloop()