from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.start_position()

    def start_position(self):
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def level_complete(self):
        return self.ycor() > FINISH_LINE_Y

    def is_colliding(self, cars):
        for car in cars:
            if self.distance(car) < 20:
                return True
        return False
