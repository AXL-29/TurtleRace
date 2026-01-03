import random
from turtle import Turtle, Screen

COLOR = ["red", "blue", "green", "yellow", "black", "orange", "purple"]
Y_COORDINATES = [200, 120, 40, -40, -120, -200]

turtles = []

screen = Screen()
screen.setup(height=500, width=800)
screen.title("Turtle Race")

for position, color in zip(Y_COORDINATES, COLOR):
    racer = Turtle("turtle")
    racer.color(color)
    racer.penup()
    racer.goto(x=-380, y=position)
    turtles.append(racer)

bet = screen.textinput(title="Place your bet!", prompt="Please enter a color to bet: ")

while True:
    for turtle in turtles:
        turtle.forward(random.randint(5, 20))

        if turtle.xcor() > 400:
            break

screen.exitonclick()