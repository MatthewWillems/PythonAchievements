i = 1000
while i > -1:
  print(i)
  i -= 1

import turtle

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)

for i in range(10):
    for colours in ["blue", "purple", "magenta", "white"]:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10)

turtle.hideturtle()
