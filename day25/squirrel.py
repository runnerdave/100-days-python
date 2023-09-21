import pandas

if __name__ == '__main__':
    df = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
    
    black_count = df[df["Primary Fur Color"] == "Black"].shape[0]
    cinnamon_count = df[df["Primary Fur Color"] == "Cinnamon"].shape[0]
    gray_count = df[df["Primary Fur Color"] == "Gray"].shape[0]

    squirrel_count_by_colours = {
        "Fur Color": ["Black", "Cinnamon", "Gray"],
        "Count": [black_count, cinnamon_count, gray_count]
    }

    print(squirrel_count_by_colours)

    squirrel_count = pandas.DataFrame(squirrel_count_by_colours)
    squirrel_count.to_csv("squirrel_by_colour_count")
