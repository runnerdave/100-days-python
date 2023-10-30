##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import os
import sys
import pandas as pd
import random


current_directory = os.path.dirname(os.path.abspath(__file__))
email_module_path = os.path.join(current_directory, "../")
sys.path.append(email_module_path)
data_directory = "data"
templates_directory = "templates"
birthdays_db_path = os.path.join(current_directory, data_directory, 'birthdays.csv')

from email_manager import send_pretend_email, get_current_date

def load_template() -> str:
    template = f"letter_{random.choice(range(1,4))}.txt"
    template_path = os.path.join(current_directory, templates_directory, template)
    with open(template_path) as t:
        return t.read()
    
def produce_letter(name) -> str:
    t = load_template()
    return t.replace("[NAME]", name)

def create_birthday_dictionary(file_path):
    birthday_dict = {}
    df = pd.read_csv(file_path)
    for _, row in df.iterrows():
        day = int(row['day'])
        month = int(row['month'])
        birthday = (day, month)
        if birthday not in birthday_dict:
            birthday_dict[birthday] = []
        birthday_dict[birthday].append([row['name'], row['email']])
    return birthday_dict

birthday_dictionary = create_birthday_dictionary(birthdays_db_path)

def main():
    current_date = get_current_date()
    birthday = (int(current_date[0]), int(current_date[1]))
    if birthday in birthday_dictionary:
        people = birthday_dictionary[birthday]
        for person in people:
            send_pretend_email(email_to=person[1], msg=produce_letter(person[0]), subject="Happy Birthday!")        
    else:
        print("No birthdays found for the given day and month.")

if __name__ == "__main__":
    main()

