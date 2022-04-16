import turtle
screen = turtle.Screen()
screen.setup(width=1.0, height=1.0, startx=None, starty=None)
screen.bgpic("BG.gif")
shape="rocketship2.gif"
screen.addshape(shape)
turtle.shape(shape)
move_speed = 20
turn_speed = 20
def forward():
  turtle.forward(move_speed)
def backward():
  turtle.backward(move_speed)
def left():
  turtle.left(turn_speed)
def right():
  turtle.right(turn_speed)
def ho():
  turtle.goto(0,0)

turtle.penup()
turtle.speed()
turtle.home()
screen.onkey(forward, "Up")
screen.onkey(backward, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(ho,"r")
screen.listen()
screen.mainloop()
