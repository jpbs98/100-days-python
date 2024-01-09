import turtle
import pandas


SCREEN = turtle.Screen()
SCREEN.title("U.S. States Game")
SCREEN.setup(width=725, height=491)
SCREEN.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")


df = pandas.read_csv("50_states.csv")


map_plotter = turtle.Turtle()
map_plotter.penup()
map_plotter.hideturtle()

states_list = df["state"].to_list()
guessed_states = []


answer_state = SCREEN.textinput(
    title="Guess the State",
    prompt="What's another state's name?",
).title()


while len(guessed_states) < 50:
    if answer_state == "Exit":
        missing_states = [state for state in states_list if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states, columns=["states"])
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in states_list:
        guessed_states.append(answer_state)
        map_plotter.goto(
            int(df[df.state == answer_state].x),  # type: ignore
            int(df[df.state == answer_state].y),  # type: ignore
        )
        map_plotter.write(answer_state)

    answer_state = SCREEN.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?",
    ).title()

turtle.done()
