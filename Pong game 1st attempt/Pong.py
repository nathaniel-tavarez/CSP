import turtle as trtl

wn = trtl.Screen()
wn.bgcolor('black')

# pong ball and walls
wall_width, wall_height = .5, 10

pong = trtl.Turtle()
pong.up()
pong.shape('circle')
pong.color('white')
pong.shapesize(float(.5))

wall2 = trtl.Turtle()
wall2.up()
wall2.shape('square')
wall2.color('blue')
wall2.shapesize(wall_width, wall_height)
wall2.goto(-350, 0)
wall2.seth(90)

wall1 = trtl.Turtle()
wall1.up()
wall1.shape('square')
wall1.color('red')
wall1.shapesize(wall_width, wall_height)
wall1.goto(350, 0)
wall1.seth(90)

wall1.hideturtle()
pong.hideturtle()
wall2.hideturtle()

angle = -180
curser_size = 20

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
    run_pong()

def run_pong():
    while True:
        pong.fd(3)
        # detect collisions between pong ball and the walls
        if collision(pong, wall1):
            pong.bk(3)
            pong.seth(abs(pong.ycor() - wall1.ycor()) * -20)
        if collision(pong, wall2):
            pong.bk(3)
            pong.seth(abs(pong.ycor() - wall2.ycor()) * -20)

def collision(a, b):
    return abs(a.xcor() - b.xcor()) < curser_size/2 + wall_width/2 and abs(a.ycor() - b.ycor()) < curser_size/2 + wall_height * curser_size


wn.onkeypress(up,"Up")
wn.onkeypress(dn, "Down")
wn.onkeypress(LL,"w")
wn.onkeypress(Ln,"s") 
wn.onkeypress(stort, "space")
wn.listen()
wn.mainloop()
