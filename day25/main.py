import csv
import pandas

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

