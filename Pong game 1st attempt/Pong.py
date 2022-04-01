import turtle as trtl
import random as Rand

# game screen setup
wn = trtl.Screen()
wn.bgcolor('black')
background = "maze3.gif"
wn.addshape(background)
wn.bgpic(background)

# pong ball and walls
wall_width, wall_height = .5, 5
border_width, border_height = 80, .5

pong = trtl.Turtle()
pong.up()
pong.shape('circle')
pong.color('black')
pong.shapesize(float(.5))

wall4= trtl.Turtle ()
wall4.up()
wall4.shape('square')
wall4.color('white')
wall4.shapesize(border_height, border_width)
wall4.goto(525, 0)
wall4.seth(90)

wall3= trtl.Turtle ()
wall3.up()
wall3.shape('square')
wall3.color('white')
wall3.shapesize(border_height, border_width)
wall3.goto(-525, 0)
wall3.seth(90)

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
bttm_border.goto(0, 300)
bttm_border.seth(90)

# score counters
scorecount1 = trtl.Turtle()
scorecount1.up()
scorecount1.goto(50, 250)
scorecount1.pd()
scorecount1.ht()

scorecount2 = trtl.Turtle()
scorecount2.up()
scorecount2.goto(-150, 250)
scorecount2.pd()
scorecount2.ht()

# variables for the game
curser_size = 20
angle = 0
poolean = True
bluescore = 0
redscore = 0
font_setup = ("Arial", 20, "normal")

# move buttons
def up():
    wall1.fd(10)
def LL():
    wall2.fd(10)
def Ln():
    wall2.bk(10)
def dn():
    wall1.bk(10)

# fun buttons
def reset():
    pong.goto(0, 0)
    pong.seth(0)
def bugfix():
    pong.seth(Rand.randint(0, 360))
def funbutton():
    global angle
    global poolean
    global bluescore
    global redscore
    poolean = False
    while poolean == False:
        pong.fd(5)
        if paddle_collision(pong, wall1):
            bugfix()
        if paddle_collision(pong, wall2):
            bugfix()
        if hrzntl_brdr_colide(pong, top_border):
            pong.seth(Rand.randint(0, 180))
        if hrzntl_brdr_colide(pong, bttm_border):
            pong.seth(Rand.randint(-180, 0))
        if scorebordercoll(pong, wall3):
            redscore += 1
            scorecount1.clear()
            scorecount1.write(redscore, font=font_setup)
            reset()
        if scorebordercoll(pong, wall4):
            bluescore += 1
            scorecount2.clear()
            scorecount2.write(bluescore, font=font_setup)
            reset()
def stop():
    wn.bye()

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

# game runs
def run_pong():
    global angle
    global bluescore
    global redscore
    while poolean == True:
        pong.fd(5)
        # detect collisions between pong ball and the walls
        if paddle_collision(pong, wall1):
            pong.bk(5)
            angle = (pong.heading() + wall1.ycor() * -1)
            if angle == 0.0:
                angle = 180
            pong.seth(angle)
            print(angle)
        if paddle_collision(pong, wall2):
            pong.bk(5)
            angle = (pong.heading() + wall2.ycor() * -1)
            if angle == 180:
                angle = 0
            pong.seth(angle)
        if hrzntl_brdr_colide(pong, top_border):
            pong.seth(Rand.randint(0, 180))
        if hrzntl_brdr_colide(pong, bttm_border):
            pong.seth(Rand.randint(-180, 0))
        if scorebordercoll(pong, wall3):
            redscore += 1
            scorecount1.clear()
            scorecount1.write(redscore, font=font_setup)
            reset()
        if scorebordercoll(pong, wall4):
            bluescore += 1
            scorecount2.clear()
            scorecount2.write(bluescore, font=font_setup)
            reset()

# collision functions
def paddle_collision(a, b):
    return abs(a.xcor() - b.xcor()) < curser_size/2 + wall_width/2 and abs(a.ycor() - b.ycor()) < curser_size/2 + wall_height * curser_size

def hrzntl_brdr_colide(a, b):
    return abs(a.xcor() - b.xcor()) < curser_size/2 + border_width * curser_size and abs(a.ycor() - b.ycor()) < curser_size/2 + border_height/2

def scorebordercoll(a, b):
    return abs(a.xcor() - b.xcor()) < curser_size/2 + wall_width * curser_size and abs(a.ycor() - b.ycor()) < curser_size/2 + 999/2

# key press sensors
wn.onkeypress(up,"Up")
wn.onkeypress(dn,"Down")
wn.onkeypress(LL,"w")
wn.onkeypress(Ln,"s") 
wn.onkeypress(bugfix,"slash")
wn.onkeypress(funbutton,"f")
wn.onkeypress(stort, "space")
wn.onkeypress(reset, "r")
wn.onkeypress(stop, "Escape")
wn.listen()
wn.mainloop()