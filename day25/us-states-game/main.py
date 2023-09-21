import turtle
import pandas

def load_data() -> pandas.DataFrame:    
    return pandas.read_csv("50_states.csv")

def find_coordinates(df: pandas.DataFrame, state: str):
    state_row = df[df.state == state.title()]
    if not state_row.empty:
        return (state_row.x.values[0], state_row.y.values[0])
    return None

if __name__ == '__main__':
    counter = 50
    screen = turtle.Screen()
    screen.title(f"US States {counter}/50")
    image = "blank_states_img.gif"
    screen.addshape(image)

    turtle.shape(image)    
    df = load_data()

    while counter > 0:
        answer_state = screen.textinput(title="Guess the State", prompt="What's another state name?")
        print(answer_state)
        pos = find_coordinates(df, answer_state)
        if pos != None: 
            counter -= 1
            print(pos)
        screen.title(f"US States {counter}/50")

    screen.exitonclick()


