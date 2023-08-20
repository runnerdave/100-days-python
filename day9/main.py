#!/usr/bin/env python3

# teacher solution: https://replit.com/@appbrewery/blind-auction-completed?v=1#main.py

from art import logo

bidders = {}


def bid():
    name = input("What is your name?")
    while True:
        try:
            bid = int(input("What is your bid?: $"))
            break
        except ValueError:
            print('Wrong choice, try again with a number!')
    bidders[name] = bid


def find_winner(bidders):
    winner = max(bidders.values())
    for key, value in bidders.items():
        if value == winner:
            return (key, value)


if __name__ == '__main__':
    print(logo)
    keep_playing = "yes"
    while keep_playing == "yes":
        bid()
        keep_playing = input(
            "Are there any other bidders? Type 'yes' or 'no'.\n")
    winner, amount = find_winner(bidders)
    print(f"The winner is {winner} with a bid of ${amount}")
