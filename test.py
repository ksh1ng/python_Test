import turtle
def triangle(torty,size):
    for i in range(2):
        torty.forward(size)
        torty.left(120)

def square(torty,size):
    for i in range(4):
        torty.forward(size)
        torty.left(90)

def rectangle(torty, width, height):
    torty.forward(height)
    torty.right(90)
    torty.forward(width)
    torty.right(90)
    torty.forward(height)
    torty.right(90)
    torty.forward(width)
    torty.right(90)
def house(torty, size, x, y):
    torty.color("red")
    torty.penup()
    torty.goto(x, y)
    torty.pendown()
    torty.setheading(90)
    square(torty, size)
    torty.forward(size)
    torty.left(30)
    triangle(torty, size)
    torty.right(90)
    torty.forward(size)
    torty.left(90)
    torty.forward(size/5)
    torty.color("black")
    torty.left(90)
    rectangle(torty, size/5, 2*size/5)

nick=turtle.Turtle()
wn=turtle.Screen()
nick.speed(1)
house(nick, 100, 10, 20)

#wn.exitonclick()
 
