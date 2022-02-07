import turtle as trtl
wn = trtl.Screen()
wn.listen()
wn.bgcolor('black')


# pong ball and walls
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

wall1.hideturtle()
pong.hideturtle()

angle = 0

# move buttons
def up():
    wall1.fd(10)

def dn():
    wall1.bk(10)

startgame = False
startbutton = trtl.Turtle()
startbutton.color('white')
startbutton.shapesize(10)
def stort():
    global startgame
    startgame = True
    wn.startscreen()
    
def startscreen():
    global wn
    if startgame == False:
        wn.mainloop()
        startbutton.onclick(stort)
        wn.listen()
        
    else:
        startbutton.hideturtle
        wall1.showturtle()
        pong.showturtle()
        wn.onkeypress(up,"Up")
        wn.onkeypress(dn, "Down")
        wn.listen()
        wn.mainloop()
        



#while (True):
#    if (abs(pong.xcor() - wall1.xcor()) < 20):
#        if (abs(pong.ycor() - wall1.ycor()) < 20):
#            pong.seth(angle + 180)


if startgame == False:
    wn.mainloop()
    wn.startscreen()
else:
    startbutton.hideturtle
    wall1.showturtle()
    pong.showturtle()
    wn.onkeypress(up,"Up")
    wn.onkeypress(dn, "Down")
    wn.listen()
    wn.mainloop()
