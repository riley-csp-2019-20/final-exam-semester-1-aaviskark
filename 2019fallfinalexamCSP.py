#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name
# Aaviskar Khatiwada
#Date
# 12/19/2019

#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors
# 
#import required libraries
import turtle as trtl
import random

#create turtle
pencil= trtl.Turtle()
pencil.shapesize(2)
#creates variables
pencil_size= 5
pencil.pensize(pencil_size)

#variable that helps determine if pencil is up or down
pencil_u=0

#list of colors
colors= ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "gray", "black"]

#movement functions
def pencil_up():
    pencil.setheading(90)
    pencil.forward(5)
def pencil_right():
    pencil.setheading(0)
    pencil.forward(5)
def pencil_left():
    pencil.setheading(180)
    pencil.forward(5)
def pencil_down():
    pencil.setheading(270)
    pencil.forward(5)

#color/drawing functions

#function to make pensize bigger
def big_pen():
    global pencil_size
    pencil_size+=1 
    pencil.pensize(pencil_size)

#function to make pensize smaller, only works if the pensize is more than 0
def small_pen():
    global pencil_size
    if pencil_size > 0:
        pencil_size= pencil_size-1
        pencil.pensize(pencil_size)

#function to make the pen go up or down
def up_down():
    global pencil_u
    if pencil_u >= 0:
        pencil.up()
        pencil_u= pencil_u-1
    else:
        pencil.down()
        pencil_u+=1
    
#function that clears the screen
def clear_pencil():
    pencil.clear()

#function that changes color randomly
def rand_color():
    pencil.pencolor(random.choice(colors))
#create screen
wn= trtl.Screen()

#bind to keypresses

#keypress to make the pencil move
wn.onkeypress(pencil_up,"Up")
wn.onkeypress(pencil_right,"Right")
wn.onkeypress(pencil_left,"Left")
wn.onkeypress(pencil_down,"Down")

#key press to make the pensize change
wn.onkeypress(big_pen,"o")
wn.onkeypress(small_pen, "p")

#keypress to make the pen go up or down
wn.onkeypress(up_down, "u")

#keypress that resets the screen
wn.onkeypress(clear_pencil, "space")

#keypress that changes the color of the pen
wn.onkeypress(rand_color, "r")
#listen
wn.listen()

#mainloop
wn.mainloop()