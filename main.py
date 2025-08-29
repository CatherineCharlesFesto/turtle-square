import turtle

turtle.Screen().bgcolor("violet")
noofsides=4
length=80
angle=360/noofsides
draw=turtle.Turtle()
for i in range (noofsides):
    draw.forward(length)
    draw.right(angle)
turtle.done()