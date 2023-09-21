import csv
import pandas

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

if __name__ == '__main__':
    with open("./weather_data.csv") as file:
        data = csv.reader(file)
        temperatures = []
        for row in data:
            if row[1] != 'temp':
                temperatures.append(int(row[1]))
            print(row)

    print(temperatures)

    df = pandas.read_csv("weather_data.csv")

    print(df)

    # get average temperature
    print(round(df['temp'].mean(), 2))

    # get row with max temperature
    print(df.loc[df.temp.idxmax()])
    print(df[df.temp == df.temp.max()])

    # get monday's temperature in fahrenheit
    monday = df[df.day == 'Monday']
    monday_temp = monday.temp[0]
    print(f'temp for monday: {monday_temp}°C / {celsius_to_fahrenheit(monday_temp)}°F')

    # create a dataframe from scratch
    data_dict = {
        "students": ["Amy", "James", "Angela"],
        "scores": [76, 56, 65]
    }
    students_df = pandas.DataFrame(data_dict)

    print(students_df)
    # produce a csv out of the students_df
    students_df.to_csv("student_scores.csv")


