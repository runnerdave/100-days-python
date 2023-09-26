import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

if __name__ == '__main__':
    #Looping through dictionaries:
    for (key, value) in student_dict.items():
        #Access key and value
        print(f"{key}:{value}")

    student_data_frame = pandas.DataFrame(student_dict)

    print("## with loop")
    #Loop through rows of a data frame
    for (index, row) in student_data_frame.iterrows():
        #Access index and row
        #Access row.student or row.score
        print(f"{index}:{row}")

    print("## with comprehension")
    # Keyword Method with iterrows()
    print({index:row for (index, row) in student_data_frame.iterrows()})

    #TODO 1. Create a dictionary in this format:
    nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
    print({row.letter:row.code for (_, row) in nato_data_frame.iterrows()})
    {"A": "Alfa", "B": "Bravo"}

    #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
    input = "Alberto"
    

