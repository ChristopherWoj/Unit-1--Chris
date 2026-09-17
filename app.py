import turtle
from turtle import *
t = Turtle()

t.shape('turtle')

sidelength = 100
rotate = 90
def square(x,y):
    for i in range(4):
        print("test")
        t.forward(x)
        t.left(y)


for i in range(60):
    square(100,90)
    
