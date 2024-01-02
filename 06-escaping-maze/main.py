# Reeborg's World - Maze
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json


def turn_right():
    turn_left()
    turn_left()
    turn_left()


# get rid of starting positions without walls on sides
while front_is_clear():
    move()
turn_left()


while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
