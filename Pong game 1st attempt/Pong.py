import turtle as trtl

wn = trtl.Screen()
wn.bgcolor('black')

# pong ball and walls
wall_width, wall_height = .5, 10
border_width, border_height = 40, .5

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

top_border = trtl.Turtle()
top_border.up()
top_border.shape('square')
top_border.color('white')
top_border.shapesize(border_width, border_height)
top_border.goto(0, -300)
top_border.seth(90)

bttm_border = trtl.Turtle()
bttm_border.up()
bttm_border.shape('square')
bttm_border.color('white')
bttm_border.shapesize(border_width, border_height)
bttm_border.goto(0, -300)
bttm_border.seth(90)

# hide all turtles before game starts
wall1.ht()
pong.ht()
wall2.ht()
top_border.ht()

curser_size = 20
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
def stort():
    startbutton.ht()
    wall1.st()
    wall2.st()
    pong.st()
    top_border.st()
    run_pong()

def run_pong():
    global angle
    while True:
        pong.fd(3)
        # detect collisions between pong ball and the walls
        if paddle_collision(pong, wall1):
            pong.bk(3)
            angle = abs(pong.ycor() - wall1.ycor()) + 180
            pong.seth(abs(pong.ycor() - wall1.ycor()) + 180)
        if paddle_collision(pong, wall2):
            pong.bk(3)
            angle = abs(pong.ycor() - wall2.ycor()) * -1
            pong.seth(abs(pong.ycor() - wall2.ycor()) * -1)
        if hrzntl_brdr_colide(pong, top_border):
            pong.bk(3)
            pong.seth(angle * -1)

def paddle_collision(a, b):
    return abs(a.xcor() - b.xcor()) < curser_size/2 + wall_width/2 and abs(a.ycor() - b.ycor()) < curser_size/2 + wall_height * curser_size

def hrzntl_brdr_colide(a, b):
    return abs(a.xcor() - b.xcor()) < curser_size/2 + border_width * curser_size and abs(a.ycor() - b.ycor()) < curser_size/2 + border_height/2

wn.onkeypress(up,"Up")
wn.onkeypress(dn, "Down")
wn.onkeypress(LL,"w")
wn.onkeypress(Ln,"s") 
wn.onkeypress(stort, "space")
wn.listen()
wn.mainloop()
