'''
Author: <ksh1ng>
Date: <2018.4.24>
Class: ISTA 130
Section Leader: <Johnny Hsu>

Description:
<hw02-(1)>
'''
import turtle
# put all of your import statements below this line and then delete this comment
def polygon(turtle,num_sides,length):
    turtle.pensize(3)
    for i in range(num_sides):
        turtle.forward(length)
        turtle.left(360/num_sides)


# put all of your function definitions below this line and then delete this comment


#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    wn=turtle.Screen()
    t1=turtle.Turtle()
    t1.speed(0)
    t2=turtle.Turtle()
    t2.speed(0)
    t3=turtle.Turtle()
    t3.speed(0)
    #draw pentagons first
    t1.color("red")
    t1.left(180)
    for j in range(5):
        polygon(t1, 5, 100)
        t1.up()
        t1.left(90)
        t1.forward(20)
        t1.right(90)
        t1.down()

    #draw square
    t2.color("blue")
    t2.left(30)
    for k in range(5):
        polygon(t2, 4, 100)
        t2.up()
        t2.forward(20)
        t2.down()

    #draw triangle
    t3.color("green")
    t3.up()
    t3.left(180)
    t3.forward(100)
    t3.right(120)
    t3.down()
    for l in range(5):
        polygon(t3, 3, 100)
        t3.up()
        t3.left(90)
        t3.forward(20)
        t3.right(90)
        t3.down()

    n.exitonclick()
    # put main code here, make sure each line is indented one level, and delete this comment
if __name__ == '__main__':
    main()

 
