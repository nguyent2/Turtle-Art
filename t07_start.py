######################################################################
# Author: Thy Nguyen and Immanuela Belaineh      TODO: Change this to your names
# Username:  belainehi & nguyent2             TODO: Change this to your usernames
#
# Assignment: T07: Turtle Art
#
# Purpose: Create beautiful works of art through code, namely iterations
#
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import turtle
import random
from math import pi

def draw_star_flower(turt):
    turt.pendown()
    for i in range (50):
        turt.color(random.random(), random.random(), random.random())
        turt.forward(50)
        turt.left(11)
        turt.forward (-50)



def draw_infinity(turt):
    # FIXME modify this function so that it's more general
    """
    Draws a randomly colored hexagon using the turtle library
    :param turt: a turtle object to draw with
    :return: None
    """
    turt.color((random.random(), random.random(), random.random()))     # gives the turtle a random color
    turt.speed(0)
    turt.penup()
    for num in range (2):
        turt.fillcolor((random.random(), random.random(), random.random()))
        turt.begin_fill()
        for i in range(180):
            turt.stamp()
            turt.forward(2)
            turt.left(2)
            turt.fillcolor((random.random(), random.random(), random.random()))
        turt.end_fill()
        turt.begin_fill()
        for i in range (180):
            turt.stamp()
            turt.forward(2)
            turt.right(2)
            turt.fillcolor((random.random(), random.random(), random.random()))
        turt.end_fill()
        turt.left(90)


def draw_icecream_cone(turt):
    # FIXME modify this function so that it's more general
    """
    Draws a randomly colored hexagon using the turtle library
    :param turt: a turtle object to draw with
    :return: None
    """
    turt.color((random.random(), random.random(), random.random()))     # gives the turtle a random color
    turt.begin_fill()
    turt.forward(120)
    turt.right(120)
    turt.forward(120)
    turt.right(120)
    turt.forward(120)
    turt.right(120)
    turt.forward(120)
    turt.left(90)
    turt.end_fill()
    turt.color((random.random(), random.random(), random.random()))
    turt.begin_fill()
    for i in range(188):
        turt.left(180/(pi*60))
        turt.forward(180/(pi*60))
    turt.end_fill()

        

def main():
    # FIXME modify the docstring so it's correct for your code
    """
    The main function which draws exactly 10 hexagons
    :return: None
    """
    t = turtle.Turtle()
    u = turtle.Turtle()
    v = turtle.Turtle()
    u.pensize(5)
    t.speed(1)
    t.shape("turtle")

    while True:
        t.penup()
        u.penup()
        # Move the turtle to a random place on the screen
        t.goto(random.randint(-300, 300), random.randint(-300, 300))
        u.setpos(t.pos())
        u.forward(-50)
        t.pendown()
        u.pendown()
        draw_infinity(t)
        draw_star_flower(u)
        draw_icecream_cone(v)

    wn.exitonclick()


if __name__ == "__main__":
    main()
