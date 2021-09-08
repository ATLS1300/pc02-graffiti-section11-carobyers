#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Caroline Byers
May 29, 2020
'''

import turtle #import the library of commands that you'd like to us


turtle.colormode(255)

# Create a panel to draw on.   
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("SeaGreen3")
panel.bgpic(image)

#=======Add your code here======
#purple earring:
turtle.up()
turtle.goto(-70,56)
turtle.down()
turtle.color("purple3","purple3")
turtle.begin_fill()
turtle.circle(8)
turtle.end_fill()
turtle.up()

#mohawk
turtle.goto(-90,140)
turtle.color("MediumVioletRed","MediumVioletRed")
turtle.down()
turtle.begin_fill()
turtle.pensize(5)
turtle.goto(-110,230)
turtle.goto(-70,210)
turtle.goto(-60,250)
turtle.goto(-40,230)
turtle.goto(-20,270)
turtle.goto(-5,220)
turtle.goto(20,260)
turtle.goto(40,200)
turtle.goto(70,230)
turtle.goto(50,180)
turtle.goto(-90,140)
turtle.end_fill()
turtle.up()

#box1
turtle.goto(250,350)
turtle.color("yellow1")
turtle.pensize(15)
turtle.down()
turtle.goto(250,300)
turtle.goto(300,300)
turtle.goto(300,350)
turtle.goto(250,350)
turtle.goto(250,300)

#box2
turtle.color("pink")
turtle.goto(250,250)
turtle.goto(200,250)
turtle.goto(200,300)
turtle.goto(250,300)
turtle.goto(250,250)
turtle.goto(200,250)

#box3
turtle.color("DarkOrange")
turtle.goto(200,200)
turtle.goto(150,200)
turtle.goto(150,250)
turtle.goto(200,250)
turtle.up()


#line
turtle.color("aquamarine")
turtle.goto(-360,-300)
turtle.pensize(25)
turtle.down()
turtle.goto(360,-300)






             





#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.done()

