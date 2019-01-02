from turtle import *
peacecolors = ("blue","black", "red3", "orange", "yellow", "seagreen4", "orchid4")
reset()
Screen()
up()
shape("turtle")
resizemode("user")
shapesize(8, 8)
goto(-320, -195)
width(70)

for pcolor in peacecolors:
    color(pcolor)
    down()
    forward(640)
    up()
    backward(640)
    left(90)
    forward(66)
    right(90)
width(25)
#设置画笔颜色
color("white")
goto(0,-170)
down()


