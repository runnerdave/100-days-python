#!/usr/bin/env python3

# teacher solution: https://replit.com/@appbrewery/band-name-generator-end

def band_name_generator():
    # your awesome code here   
    print('Welcome to the Band Name Generator.') 
    city = input('What\'s the name of the city you grew up in?\n')
    pet = input('What\'s your pet\'s name?\n')
    print(f'Your band name could be {city} {pet}')


if __name__ == '__main__':
    band_name_generator()
