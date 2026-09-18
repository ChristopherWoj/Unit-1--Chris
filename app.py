import turtle
from turtle import *
t = Turtle()

t.shape('turtle')

sidelength = 100
rotate = 90

def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)


def doubleSquares(iRange):
    length = 5
    for i in range(iRange):
        square(length, 90)
        length = length + 5
doubleSquares(1)


for i in range (60):
    doubleSquares(2)
    t.right(5)

