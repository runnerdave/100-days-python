#!/usr/bin/env python3

# teacher solution: https://replit.com/@appbrewery/Day-7-Hangman-Final?v=1#main.py

import random

from ascii_art import stages, ascii_title

from words import word_list
# word_list = ["aardvark", "baboon", "camel"]
chances = len(stages) - 1
word = ""
progress = ""

def choose_word():
    global word, progress
    word = random.choice(word_list)
    progress = ['_' for _ in range(len(word))]
    return 

def check_guess(guess):
    global chances
    if guess in word:
        return True
    chances -=  1
    return False

def check_if_complete():
    if not "_" in progress:
        print("You won!")
        return True
    return False

def update_progress(guess):
    positions = [index for index, char in enumerate(word) if char == guess]
    for i in positions:
        progress[i] = guess


def play():
    print(ascii_title)
    choose_word()
    while chances > 0:
        guess = input('Guess a letter:')
        if check_guess(guess):
            update_progress(guess)            
            if check_if_complete():
                return
        else:
            print(f'You guessed {guess}, that\'s not in the word. You lose a life.')
            
        print(progress)
        print(stages[chances])
    print("You lose!")
    print(f'Word was: {word}')


if __name__ == '__main__':
    play()
