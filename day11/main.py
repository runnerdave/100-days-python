#!/usr/bin/env python3

# teacher solution: https://replit.com/@appbrewery/blackjack-final?v=1

# instructions

# Do you want to play a game of Blackjack? Type 'y' or 'n': 
#    Your cards: [5, 10], current score: 15
#    Computer's first card: 9
# Type 'y' to get another card, type 'n' to pass: 

from art import logo
from cards import Deck

import os
   
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

deck = Deck()
deck.shuffle()

messages = {
    "you_win": "You win 😃",
    "you_lose": "You lose 😤",
    "you_over": "You went over. You lose 😭",
    "comp_over": "Opponent went over. You win 😁",
    "draw": "Draw 🙃",
}

def draw_round():
    user_cards = []
    for _ in range(2):
        user_cards.append(deck.draw_card())
    computer_cards = [deck.draw_card()]
    return user_cards, computer_cards

def sum_hand(cards):
    hand = 0
    for c in cards:
        if c.rank.isnumeric():
            hand += int(c.rank)
        elif c.rank == "Ace":
            hand += 1
        else:
            hand += 10
    return hand

def show_hands(user_cards, computer_cards):
    print(f"  Your cards: {user_cards}, current score: {sum_hand(user_cards)}")
    print(f"  Computer's first card {computer_cards}: {sum_hand(computer_cards)}")

def determine_winner(user_cards, computer_cards):
    user = sum_hand(user_cards)
    comp = sum_hand(computer_cards)
    result = user - comp
    if result > 0:
        print(messages["you_win"])
    elif result < 0:
        print(messages["you_lose"])
    else:
        print(messages["draw"])

def computer_draws(computer_cards):
    while sum_hand(computer_cards) <= 17:
        computer_cards.append(deck.draw_card())
    return computer_cards

def play():
    while True:
        finish_early = False
        keep_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if keep_playing != 'y':
            break
        user_cards, computer_cards = draw_round()
        show_hands(user_cards, computer_cards)
        draw_more = 'y'
        while draw_more == 'y':
            draw_more = input("Type 'y' to get another card, type 'n' to pass: ")
            if draw_more != 'y':
                computer_draws(computer_cards)
                show_hands(user_cards, computer_cards)
                if sum_hand(computer_cards) > 21:
                    print(messages["comp_over"])  
                    finish_early = True                  
                break
            user_cards.append(deck.draw_card())
            show_hands(user_cards, computer_cards)
            if sum_hand(user_cards) > 21:
                print(messages["you_over"])
                finish_early = True 
                break
        if not finish_early:
            determine_winner(user_cards, computer_cards)        

if __name__ == '__main__':
    print(logo)    
    play()
