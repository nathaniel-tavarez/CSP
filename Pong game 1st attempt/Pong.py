
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





if paddle_collision(pong, wall3):
            print("point")
            pong.goto(0,0)  
        if paddle_collision(pong, wall4):
            print("point") 
