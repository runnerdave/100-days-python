#!/usr/bin/env python3

# teacher solution: https://replit.com/@appbrewery/calculator-final?v=1

from art import logo


# What's the first number?: 56
# +
# -
# *
# /
# Pick an operation: /
# What's the next number?: 2
# 56.0 / 2.0 = 28.0
# Type 'y' to continue calculating with 28.0, or type 'n' to start a new calculation: 

def sum(a, b):
    return a + b

def minus(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

operations = {
    '+': sum,
    '-': minus,
    '*': multiply,
    '/': divide,
}

def calculate():
    keep_going = 'y'
    result = None
    while keep_going == 'y':
        try: 
            if result is not None:                
                a = result  
            else:
                a = int(input("What's the first number?: "))
            op = input("+\n-\n*\n/\nPick an operation: ")
            b = int(input(" What's the next number?: "))
            result = operations[op](a, b)
        except ValueError:
            print('Enter only numbers, start again')
            continue
        except KeyError:
            print('Enter a valid operations, start again')
            continue
        print(f"{a} {op} {b} = {result}")
        keep_going = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:\n")


if __name__ == '__main__':
    print(logo)
    calculate()