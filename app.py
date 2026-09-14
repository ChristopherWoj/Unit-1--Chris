import turtle
from turtle import *
t = Turtle()

t.shape('turtle')
def square(x):
    t.forward(x)
    t.left(180)
    t.forward(x)
    t.left(180)
    t.forward(x)
    t.left(180)
    t.forward(x)
    t.left(180)
square(100)



turtle.done()

def message(input):
    print(input)
message("Hello Class")

