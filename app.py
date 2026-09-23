import turtle
from turtle import *
t = Turtle() 

t.shape('turtle')

sidelength = 100
rotate = 90
length_history=[]

""" def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)


def doubleSquares(iRange):
    length = 5
    for i in range(iRange):
        square(length, 90)
        length = length + 5
doubleSquares(1) """


def spiral(x):
    sidelength = 5
    for i in range (x):
        for i in range (4):
            t.forward(sidelength)
            t.right(90)
        sidelength += 5
        t.right(5)
spiral(60)
