import pandas
import os

current_directory = os.path.dirname(os.path.abspath(__file__))

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
    nato_phonetic_alphabet = "nato_phonetic_alphabet.csv"
    file_path = os.path.join(current_directory, nato_phonetic_alphabet)
    nato_data_frame = pandas.read_csv(file_path)
    nato_dict = {row.letter:row.code for (_, row) in nato_data_frame.iterrows()}
    print(nato_dict)
    # {"A": "Alfa", "B": "Bravo"}

    #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
    word = input('Enter the word to translate to NATO code:')
    try:
        codes = [nato_dict[l.upper()] for l in word]
    except KeyError as error:
        print("Sorry, only letters in the alphabet")
    else:
        print(codes)
