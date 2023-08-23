# teacher solution: https://replit.com/@appbrewery/guess-the-number-final#main.py

#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

# sample run:

# Welcome to the Number Guessing Game!
# I'm thinking of a number between 1 and 100.
# Pssst, the correct answer is 71
# Choose a difficulty. Type 'easy' or 'hard':
# You have 5 attempts remaining to guess the number.
# Make a guess: 63
# Too high.
# Guess again.

from art import logo

def play():
    return

if __name__ == '__main__':
    print(logo)
    play()