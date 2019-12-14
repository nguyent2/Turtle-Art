######################################################################
# Author: Thy H. Nguyen     TODO: Change this to your names
# Username: nguyent2             TODO: Change this to your usernames
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


def draw_icecream_cone(turt):
    # FIXME modify this function so that it's more general
    """
    Draws a randomly colored hexagon using the turtle library
    :param turt: a turtle object to draw with
    :return: None
    """
    turt.color((random.random(), random.random(), random.random()))     # gives the turtle a random color
    turt.forward(120)
    turt.right(120)
    turt.forward(120)
    turt.right(120)
    turt.forward(120)
    turt.right(120)
    turt.forward(120)
    turt.left(90)
    for i in range(180):
        turt.forward(1)
        turt.left(180/(pi*60))


def main():
    # FIXME modify the docstring so it's correct for your code
    """
    The main function which draws infinite hexagon.
    :return: None
    """
    t = turtle.Turtle()
    wn = turtle.Screen()

    # Draws 10 hexagons
    #for num in range(10):
    while 1>0:
        #while 1>0 is true, the program will runs
        # As 1>0 is the fact, this will be an infinite loop.
        t.penup()
        # Move the turtle to a random place on the screen
        t.goto(random.randint(-300, 300), random.randint(-300, 300))
        t.pendown()

        draw_icecream_cone(t)

    wn.exitonclick()

if __name__ == "__main__":
    main()
