from turtle import Screen
from snake import Snake
import time


GAME_IS_ON = True
SCREEN = Screen()
SCREEN.setup(width=600, height=600)
SCREEN.bgcolor("black")
SCREEN.title("Snake Game")
SCREEN.tracer(0)


snake = Snake()

SCREEN.listen()
SCREEN.onkey(snake.up, "Up")
SCREEN.onkey(snake.down, "Down")
SCREEN.onkey(snake.left, "Left")
SCREEN.onkey(snake.right, "Right")


while GAME_IS_ON:
    SCREEN.update()
    time.sleep(0.05)

    snake.move()

SCREEN.exitonclick()
