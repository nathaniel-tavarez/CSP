import turtle as trtl

pong = trtl.Turtle()
pong.up()
pong.shape('circle')
pong.color('white')
pong.shapesize(float(.5))
wall1 = trtl.Turtle()
wall1.up()
wall1.shape('square')
wall1.color('white')
wall1.shapesize(.5, 10, .5)
wall1.goto(350, 0)
wall1.seth(90)
angle = 0

def up():
    wall1.fd(10)

def dn():
    wall1.bk(10)

#c = 1
#while (c < 2):
#    if (abs(pong.xcor() - wall1.xcor()) < 20):
#        if (abs(pong.ycor() - wall1.ycor()) < 20):
#            pong.seth(0 + 180)


wn = trtl.Screen()
wn.onkeypress(up,"Up")
wn.onkeypress(dn, "Down")
wn.listen()
wn.bgcolor('black')
wn.mainloop()
