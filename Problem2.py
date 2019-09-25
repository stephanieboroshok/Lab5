# turtle
# import turtle
# create turtle
# draw things
#create a fucntion that takes in parameter length to determine length of square

import turtle

def square (turtle_obj,length):
    for i in range(4):
        turtle_obj.fd(length)
        turtle_obj.rt(90)

length = int(input('Enter the length of the sides of the square:'))
bob = turtle.Turtle()

square(bob, length)

turtle.done()
# keeps window open