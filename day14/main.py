# teacher solution: https://replit.com/@appbrewery/higher-lower-final?v=1#art.py


import random
from art import logo, vs
from game_data import data


def compare(a, b):
    if a > b:
        return "A"
    elif b > a:
        return "B"
    else:
        return "None"
    
def print_data(a):
    return(f"{a['name']}, a {a['description']}, from {a['country']}")


def play():
    winning = True
    wins = 0
    while winning:
        a = random.choice(data)
        data.remove(a)
        b = random.choice(data)
        data.remove(b)
        print(f"Compare A: {print_data(a)}")
        print(vs)
        print(f"Against B: {print_data(b)}")
        choice = input(f"Who has more followers?\n")
        if choice.upper() == compare(a['follower_count'], b['follower_count']):
            wins += 1
            print(f"You're right! Current score: {wins}")
            continue
        else:
            print(f"Sorry, that's wrong. Final score: {wins}")
            break

    return


if __name__ == '__main__':
    print(logo)
    play()
