'''
Author: <ksh1ng>
Date: <2018.4.24>
Class: ISTA 130
Section Leader: <Johnny Hsu>

Description:
<hw01-(2)>
'''
import turtle
# put all of your import statements below this line and then delete this comment
def  triangle(t,size):
    for i in range(3):
        t.forward(size)
        t.left(120)
def  square(t,size):
    for i in range(4):
        t.forward(size)
        t.right(90)

def  pentagon(t,size):
    for i in range(5):
        t.forward(size)
        t.right(72)

def  hexagon(t,size):
    for i in range(6):
        t.forward(size)
        t.left(60)

# put all of your function definitions below this line and then delete this comment


#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    nick=turtle.Turtle()
    wn=turtle.Screen()
    wn.setworldcoordinates(-400,-400,400,400)
    nick.speed(0)
    nick.pensize(10)


    nick.right(90)
    nick.color("goldenrod")
    hexagon(nick,100)
    nick.color("red")
    triangle(nick,100)
    nick.up()
    nick.left(60)
    nick.forward(100)
    nick.down()
    triangle(nick,100)
    nick.up()
    nick.forward(100)
    nick.left(120)
    nick.down()
    nick.color("black")
    pentagon(nick,100)
    nick.up()
    nick.home()
    nick.left(90)
    nick.forward(-100)
    nick.down()
    nick.color("goldenrod")
    hexagon(nick,100)
    nick.color("red")
    triangle(nick,100)
    nick.left(60)
    nick.forward(200)
    nick.left(120)
    triangle(nick,100)
    nick.color("black")
    square(nick,100)
    nick.right(90)
    nick.forward(100)
    nick.right(90)
    nick.forward(-100)
    nick.color("lightgreen")
    triangle(nick,100)

    wn.exitonclick()
    # put main code here, make sure each line is indented one level, and delete this comment



    #input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()

 
