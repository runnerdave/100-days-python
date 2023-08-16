#!/usr/bin/env python3

# teacher solution: https://replit.com/@appbrewery/rock-paper-scissors-end

# Instructions
# Make a rock, paper, scissors game.

# Inside the main.py file, you'll find the ASCII art for the hand signals already saved to a corresponding variable: rock, paper, and scissors. 
# This will make it easy to print them out to the console.

# Start the game by asking the player:

# "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

# From there you will need to figure out:

# How you will store the user's input.
# How you will generate a random choice for the computer.
# How you will compare the user's and the computer's choice to determine the winner (or a draw).
# And also how you will give feedback to the player.
# You can find the "official" rules of the game on the World Rock Paper Scissors Association website.

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choices = [rock, paper, scissors]

rules = {
    (0, 1): "lose",
    (0, 2): "win",
    (1, 0): "win",
    (1, 2): "lose",
    (2, 0): "lose",
    (2, 1): "lose",
}

def play_paper_scissors_rock():
    while 1==1:
        user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
        if user_choice < 0 or user_choice > 2:
            print('Wrong choice')
            return
        print(f'You chose:\n{choices[user_choice]}')
        computer_choice = random.randint(0, 2)
        print(f'Computer chose:\n{choices[computer_choice]}')
        if user_choice == computer_choice:
            print('Result: draw')
            continue
        print(f'Result:{rules[user_choice, computer_choice]}')

if __name__ == '__main__':
    play_paper_scissors_rock()