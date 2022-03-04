import turtle, pandas
from turtle import Screen
from action import write_state
#Basic Setup of the display
image = "blank_states_img.gif"
screen = Screen()
screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)

#Get the State Information from csv file:
data = pandas.read_csv("50_states.csv")
states_all = data.state.to_list()

#Create the user guessed data in background
guessed_states = []
missing_states = []
#let user keep guessing until manually quit
while len(guessed_states) < 50:
    answer_state = screen.textinput(f'{len(guessed_states)}/50 State Correct', prompt="What's another state's name?")
    if answer_state:
        valid_answer_state = answer_state.title()
        if valid_answer_state in states_all and valid_answer_state not in guessed_states:
            guessed_states.append(valid_answer_state)
            #show the state name guessed onto the map
            x = int(data[data['state'] == valid_answer_state].x)
            y = int(data[data['state'] == valid_answer_state].y)
            write_state(x, y, valid_answer_state)
    else:
        for state in states_all:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

screen.exitonclick()