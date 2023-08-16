#!/usr/bin/env python3

# teacher solution: https://replit.com/@appbrewery/tip-calculator-end?v=1

def tip_calculator():
    # your awesome code here   
    print('Welcome to the tip calculator!') 
    total = input('What was the total bill? $')
    tip = input('How much tip would you like to give? 10, 12, or 15? ')
    people = input('How many people to split the bill? ')
    print(f'Each person should pay: $ {round((int(total) + int(tip))/int(people), 2)}')

if __name__ == '__main__':
    tip_calculator()