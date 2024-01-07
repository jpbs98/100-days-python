import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


GAME_IS_ON = True
SCREEN = Screen()
SCREEN.setup(width=800, height=600)
SCREEN.bgcolor("black")
SCREEN.title("Pong")
SCREEN.tracer(0)


paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

SCREEN.listen()
SCREEN.onkey(paddle_right.up, "Up")
SCREEN.onkey(paddle_right.down, "Down")
SCREEN.onkey(paddle_left.up, "w")
SCREEN.onkey(paddle_left.down, "s")

while GAME_IS_ON:
    time.sleep(ball.move_speed)
    SCREEN.update()
    ball.move()

    # collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # collision with paddle
    if (
        ball.distance(paddle_right) < 50
        and ball.xcor() > 320
        or ball.distance(paddle_left) < 50
        and ball.xcor() < -320
    ):
        ball.reverse()
        ball.increase_speed()

    # ball out of bounds
    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.left_point()

    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.right_point()


SCREEN.exitonclick()
