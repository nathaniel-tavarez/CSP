from tkinter import Image
import turtle as trtl
wn = trtl.Screen()

# pong ball and walls
pong = trtl.Turtle()
pong.up()
pong.shape('circle')
pong.color('green')
pong.shapesize(float(.8))
wall2 = trtl.Turtle()
wall2.up()
wall2.shape('square')
wall2.color('blue')
wall2.shapesize(.5, 10, .5)
wall2.goto(-350, 0)
wall2.seth(90)

wall1 = trtl.Turtle()
wall1.up()
wall1.shape('square')
wall1.color('red')
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
def stort():
    startbutton.ht()
    wall1.st()
    wall2.st()
    pong.st()
    while (True):
        pong.fd(2)
        # detect collisions between pong ball and the walls
        wn_canvas = wn.getcanvas()
        x,y = pong.position()
        margin = 5
        items = wn_canvas.find_overlapping(x+margin, -y+margin, x-margin, -y-margin)
        # check if canvas is not empty
        if (len(items) > 0):
            print(items[0])
            # get property of lowest object (canvas)
            canvas_color = wn_canvas.itemcget(items[0], 'fill')
            if canvas_color == wall1.color():
                pong.seth(angle + 45)


#while (True):
#    if (abs(pong.xcor() - wall1.xcor()) < 20):
#        if (abs(pong.ycor() - wall1.ycor()) < 20):
#            pong.seth(angle + 180)

wn.bgpic("maze3.png")
wn.listen()
wn.onkeypress(up,"Up")
wn.onkeypress(dn, "Down")
wn.onkey(LL,"w")
wn.onkey(Ln,"s") 
wn.onkeypress(stort, "space")
wn.listen()
wn.mainloop()
