import random
import turtle
import colorgram


colors = colorgram.extract("image.jpg", 30)

rgb_codes = []
for color in colors:
    r = color.rgb[0]
    g = color.rgb[1]
    b = color.rgb[2]
    rgb_codes.append((r, g, b))


# slice off background colors
rgb_codes = rgb_codes[5:]


t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)

START_X = -250
START_Y = -250

for _ in range(10):
    t.penup()
    t.goto(START_X, START_Y)
    for _ in range(10):
        t.dot(20, random.choice(rgb_codes))
        t.penup()
        t.fd(50)
    START_Y += 50

t.hideturtle()

turtle.mainloop()
