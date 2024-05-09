import turtle
import pandas
from state import State

screen = turtle.Screen()
screen.title("Indian_States")
image = "indian_map.gif"
screen.addshape(image)
tur = turtle.Turtle()
tur.shape(image)

s = State()

data = pandas.read_csv("29_states.csv")
states = data["state"]
list_ser = states.tolist()


score = 0
all_states_unions = 36
guessed_state = set()


game_is_on = True

while game_is_on:
    users_guess = screen.textinput(title=f"guess the state {score} / {all_states_unions}", prompt="name the state")
    if users_guess.title() not in guessed_state:
        if users_guess.title() in list_ser:
            state_data = data[data.state == users_guess.title()]
            x_cor = int(state_data.x)
            y_cor = int(state_data.y)
            s.goto(x_cor, y_cor)
            s.write(arg=users_guess.title() , align= "center" , font=("Arial",12,"normal"))
            score += 1
            guessed_state.add(users_guess.title())


    if score == all_states_unions:
        game_is_on = False


screen.mainloop()