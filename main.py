import turtle
import pandas as pd

states = pd.read_csv("50_states.csv")
state_list = states.state.to_list()
screen = turtle.Screen()
image = "blank_states_img.gif"
screen.title("U.S. State Game")
screen.bgpic(image)
score = 0

while score != 50:
    answer_state = screen.textinput(title=f" {score}/50 States Correct", prompt="What's another states name?").title()
    if answer_state in state_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states[states.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        score += 1
        state_list.remove(answer_state)
    if answer_state == "Exit":
        missed_states = pd.DataFrame(state_list).to_csv("learn_states.csv")
        print(missed_states)
        break
