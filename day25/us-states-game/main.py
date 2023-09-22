import turtle
import pandas

FONT = ("Arial", 16, "normal")

guesses = []


def check_if_guessed(state):
    if state in guesses:
        return True
    else:
        guesses.append(state)
        return False


def dump_missed_states(df: pandas.DataFrame):
    for state in guesses:
        state_row = df[df.state == state]
        if not state_row.empty:
            df = df.drop(state_row.index, axis=0)
    df.to_csv("missed_states.csv")


def load_data() -> pandas.DataFrame:
    return pandas.read_csv("50_states.csv")


def find_coordinates(df: pandas.DataFrame, state: str):
    state_row = df[df.state == state]
    if not state_row.empty:
        return (state_row.x.values[0], state_row.y.values[0])
    return None


def tag_state(pos, name):
    t = turtle.Turtle(visible=False)
    t.color("black")
    t.up()
    t.goto(pos)
    t.write(name, font=FONT)


if __name__ == '__main__':
    counter = 50
    screen = turtle.Screen()
    screen.title(f"US States {counter}/50")
    image = "blank_states_img.gif"
    screen.addshape(image)

    turtle.shape(image)
    df = load_data()

    while counter > 0:
        answer_state = screen.textinput(
            title="Guess the State", prompt="What's another state name?")
        print(answer_state)
        answer_state = answer_state.title()
        if answer_state == "Exit":
            dump_missed_states(df)
            break
        pos = find_coordinates(df, answer_state)
        if not check_if_guessed(answer_state) and pos != None:
            counter -= 1
            tag_state(pos, answer_state)
        screen.title(f"US States {counter}/50")

    screen.exitonclick()
