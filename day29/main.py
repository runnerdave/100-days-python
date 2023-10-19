import pyperclip 
import random
from tkinter import *
from tkinter import messagebox
import os
current_directory = os.path.dirname(os.path.abspath(__file__))

logo = "./logo.png"
file_path = os.path.join(current_directory, logo)

db = "./db.txt"

FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

keyboard_layout = list("`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>?")

def generate_password():
    new_password = random.choice(keyboard_layout)
    password_entry.insert(0, string=new_password)
    pyperclip.copy(new_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def write_database(output):
    with open(f"{db}", "a") as path:
        path.write(output)


def add_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    output = f"{website} | {username} | {password}\n"

    if website == "":
        messagebox.showerror(message="website is empty")
    else:
        is_ok = messagebox.askokcancel(message=f"are you happy with the following result:\n{output}", icon=messagebox.INFO)
        if is_ok:
            write_database(output)
            website_entry.delete(first=0, last=END)
            username_entry.delete(first=0, last=END)
            password_entry.delete(first=0, last=END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
padlock_img = PhotoImage(file=file_path)
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=(FONT_NAME, 25))
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:", font=(FONT_NAME, 25))
username_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=(FONT_NAME, 25))
password_label.grid(column=0, row=3)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
