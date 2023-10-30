import os
import random
import smtplib
import datetime as dt

current_directory = os.path.dirname(os.path.abspath(__file__))
images_directory = "images"
data_directory = "data"

my_email = os.environ.get("EMAIL")
my_pass = os.environ.get("PASS")


def send_email(email_to, msg, email_from=my_email, subject='Subject', passw=my_pass):
    with smtplib.SMTP("outlook.office365.com") as connection:
        connection.starttls()
        connection.login(user=email_from, password=passw)
        # msg="Subject:My subject\n\nHello world"
        connection.sendmail(from_addr=email_from, to_addrs=email_to,
                            msg=f"Subject:{subject}\n\n{msg}")


def send_pretend_email(email_to, msg, email_from=my_email, subject='Subject', passw=my_pass):
    print(f"email sent to:{email_to}, from:{email_from} with password:{passw}")
    print(f"Subject:{subject}\n\n{msg}")


def get_current_day_of_the_week():
    current_date = dt.datetime.now()
    day_of_week = current_date.strftime("%A")
    return day_of_week


def get_current_date():
    current_date = dt.datetime.now()
    day = current_date.strftime("%d")
    month = current_date.strftime("%m")
    year = current_date.strftime("%Y")
    return (day, month, year)


def get_random_quote():
    with open(os.path.join(current_directory, data_directory, 'quotes.txt'), 'r') as file:
        lines = file.readlines()
        random_line = random.choice(lines).strip()
        return random_line

# if get_current_day_of_the_week() == 'Monday':
#     send_pretend_email("jane.doe@hotmail.com", get_random_quote())
