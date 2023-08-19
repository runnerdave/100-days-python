#!/usr/bin/env python3

# teacher solution: https://replit.com/@appbrewery/caesar-cipher-completed?v=1#main.py

from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def shift_letters(message, forward, shift):
    indices = []
    for l in message:
        for i, char in enumerate(alphabet):
            if char == l:
                indices.append(i)
                break
    if forward:
        shifted_indices = [i + shift for i in indices]
    else:
        shifted_indices = [i - shift for i in indices]
    return ''.join([alphabet[i] for i in shifted_indices])

# the following is the ai generated version

import string

alphabet_ai = string.ascii_lowercase

def shift_letters_ai(message, forward, shift):
    indices = [alphabet.index(char) for char in message]
    shifted_indices = [i + shift if forward else i - shift for i in indices]
    return ''.join([alphabet[i % len(alphabet)] for i in shifted_indices])

# end ai generated version


def cipher():
    keep_going = "yes"
    while keep_going == "yes":
        function = input(
            "Type 'encode' to encrypt, type 'decode' to decrypt (default entry is encode):")
        message = input("Type your message:")
        try:
            shift = int(input("Type the shift number:"))
        except ValueError:
            print('Wrong choice, try again with a number!')
            continue
        end_text = shift_letters(message, function != "decode", shift)
        print(f"Here's the {function}d result: {end_text}")
        keep_going = input(
            "Type 'yes' if you want to go again. Otherwise type 'no'.")


if __name__ == '__main__':
    print(logo)
    cipher()
