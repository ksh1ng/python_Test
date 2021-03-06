import random
import turtle


def isInScreen(w, t):

    leftBound = -(w.window_width() / 2)
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -(w.window_height() / 2)

    turtleX = t.xcor()
    turtleY = t.ycor()


    if turtleX>rightBound or turtleX<leftBound or turtleY>topBound or turtleY<bottomBound:
        return False

    else:
        return True

nick = turtle.Turtle()
wn = turtle.Screen()

nick.shape('turtle')
while isInScreen(wn, nick):
    coin = random.randrange(0, 2)
    if coin == 0:              # heads
        nick.left(90)
    else:                      # tails
        nick.right(90)

    nick.forward(50)

wn.exitonclick()
 
 
