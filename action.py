from turtle import Turtle

def write_state(x,y,state_name):
    tt = Turtle()
    tt.hideturtle()
    tt.penup()
    tt.goto(x,y)
    tt.write(state_name)