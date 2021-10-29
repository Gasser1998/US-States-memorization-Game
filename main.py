import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. Stats Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(800, 500)
hobbs = turtle.Turtle()
hobbs.hideturtle()
hobbs.pu()
play = True
score = 0
states = pandas.read_csv("50_states.csv")
states_not_guessed = states.state.to_list()

while play is True:
    if score == 50:
        play = False

    answer_state = screen.textinput(title=f"{score}/50 States correct", prompt="What's another state's name?").title()
    if answer_state == 'Exit':
        states_missed = pandas.DataFrame(states_not_guessed)
        states_missed.to_csv("States_missed.csv")
        exit()

    for S in range(len(states.state)):
        xcor = states.x[S]
        ycor = states.y[S]
        if answer_state == states.state[S]:
            states_not_guessed.remove(states.state[S])
            score += 1
            hobbs.goto(xcor,ycor)
            hobbs.write(arg=F"{answer_state}",move=False,align="center",font=("Arial",8,"normal"))
        elif answer_state == "exit":
            states_not_guessed.to_csv("States_missed.csv")
            break
