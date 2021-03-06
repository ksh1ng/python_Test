'''
Initial code for Homework 2: Part 2

This program uses turtle graphics to draw a castle.
'''

import turtle


def polygon(turtle,num_sides,length):

    for i in range(num_sides):
        turtle.forward(length)
        turtle.left(360/num_sides)
    return None

def house(a_turtle, size):
    '''Draw a simple house of the given size.'''
    polygon(a_turtle,4,size)
    a_turtle.left(90)
    a_turtle.forward(size)
    a_turtle.right(90)
    polygon(a_turtle,3,size)
    a_turtle.left(90)
    a_turtle.backward(size)
    a_turtle.right(90)
    return None


def castle(a_turtle, size):
    '''Draw a simple castle of the given size.'''
    polygon(a_turtle,4,size)
    a_turtle.penup()
    a_turtle.backward(size * 0.25)
    a_turtle.left(90)
    a_turtle.forward(size)
    a_turtle.right(90)
    a_turtle.pendown()
    house(a_turtle, size * 0.5)
    a_turtle.forward(size * 0.5)
    house(a_turtle, size * 0.5)
    a_turtle.forward(size * 0.5)
    house(a_turtle, size * 0.5)
    a_turtle.penup()
    a_turtle.backward(size * 0.75)
    a_turtle.left(90)
    a_turtle.backward(size)
    a_turtle.right(90)
    a_turtle.pendown()
    return None

#==============================================
def main():
    '''Draw a castle.'''
    yertle = turtle.Turtle()
    wn=turtle.Screen()
    yertle.speed(0)
    yertle.penup()
    yertle.backward(100)
    yertle.pendown()
    yertle.pencolor('dark slate grey')
    yertle.pensize(5)
    for j in range(4):
        castle(yertle, 100)
        yertle.forward(100)
    yertle.right(180)
    for k in range(4):
        castle(yertle, 100)
        yertle.forward(100)


    wn.exitonclick()

if __name__ == '__main__':
    main()

 
