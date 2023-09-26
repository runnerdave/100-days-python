

if __name__ == '__main__':
    # double
    l = range(1, 5)
    print(l)
    print([d*2 for d in l ])
    
    l2 = [1,1,2,3,5,8,13,21,34,55]
    # square
    print([n**2 for n in l2])
    # even
    print([n for n in l2 if n%2 == 0])

    # dictionary comprehension
    sentence = "How many angels fit in the head of a needle"
    sentence2 = "What is the Airspeed Velocity of an Unladen Swallow?"
    word_dict = {word: len(word) for word in sentence2.split()}
    print(word_dict)

    # temp conversion over a dictionary
    temp_c = {'Monday': '12', 'Tuesday': '14', 'Wednesday': '15', 'Thursday': '14', 'Friday': '21', 'Saturday': '22', 'Sunday': '24'}

    print(f"Celsius:\n{temp_c}")

    # print(f"Fahrenheit:\n{day: ((int(celsius) * 9/5) + 32) for day, celsius in temp_c} ")
    temp_f = {day: str((int(celsius) * 9/5) + 32) for day, celsius in temp_c.items()}
    print(f"Fahrenheit:\n{temp_f} ")