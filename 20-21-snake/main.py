import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


GAME_IS_ON = True
SCREEN = Screen()
SCREEN.setup(width=600, height=600)
SCREEN.bgcolor("black")
SCREEN.title("Snake Game")
SCREEN.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()


SCREEN.listen()
SCREEN.onkey(snake.up, "Up")
SCREEN.onkey(snake.down, "Down")
SCREEN.onkey(snake.left, "Left")
SCREEN.onkey(snake.right, "Right")


while GAME_IS_ON:
    SCREEN.update()
    time.sleep(0.05)

    snake.move()

    # collision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()
        scoreboard.update_scoreboard()

    # collision with wall
    if (
        snake.segments[0].xcor() > 280
        or snake.segments[0].xcor() < -280
        or snake.segments[0].ycor() > 280
        or snake.segments[0].ycor() < -280
    ):
        GAME_IS_ON = False
        scoreboard.game_over()

    # collision with tail
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            GAME_IS_ON = False
            scoreboard.game_over()


SCREEN.exitonclick()
