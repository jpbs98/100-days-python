import random
from turtle import Turtle, Screen


X_AXIS = -230
Y_AXIS = -100
RACE = True


SCREEN = Screen()
SCREEN.setup(width=500, height=400)
user_bet = SCREEN.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []


for i, color in enumerate(colors):
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(X_AXIS, Y_AXIS)
    Y_AXIS += 40
    all_turtles.append(turtle)


while RACE:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            RACE = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"You've won! The {winner_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winner_color} turtle is the winner!")

        turtle.forward(random.randint(0, 10))


SCREEN.exitonclick()
