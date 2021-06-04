import turtle
import pandas as pd
import random
screen = turtle.Screen()
screen.title("Map Indian States")
image = "Indian_Map.gif"
screen.addshape(image)
turtle.shape(image)
COLORS = ['red', 'green', 'yellow', 'magenta', 'dark blue', 'orange', 'brown']

# def get_co_ordinates(x, y):
#     print(x, y)
# turtle.onscreenclick(get_co_ordinates)
scoreboard = 0
states_df = pd.read_csv("Indian_states.csv")
states_list = states_df.States.tolist()
guessed_states = []
on = True
while on:
    guess = screen.textinput(f"{scoreboard}/28 States correct", prompt="What is Next State name of India?")
    answer = guess.title()
    if answer == "Exit":
        missing_state = []
        for state in states_list:
            if state not in guessed_states:
                missing_state.append(state)
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv('states_to _learn')
        break
    if answer in states_list:
        p = turtle.Turtle()
        p.hideturtle()
        p.penup()
        p.color(random.choice(COLORS))
        data = states_df[states_df.States == answer]
        p.goto(int(data.x), int(data.y))
        p.write(answer)
        guessed_states.append(answer)
        scoreboard += 1
    if scoreboard == 28:
        on = False

turtle.mainloop()