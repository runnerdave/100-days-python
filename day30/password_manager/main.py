import json
import pyperclip 
import random
from tkinter import *
from tkinter import messagebox
import os
current_directory = os.path.dirname(os.path.abspath(__file__))

logo = "./logo.png"
logo_path = os.path.join(current_directory, logo)

db = "./db.json"
db_path = os.path.join(current_directory, db)

FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

keyboard_layout = list("`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>?")

def generate_password():
    new_password = "".join([random.choice(keyboard_layout) for _ in range(6)])
    password_entry.insert(0, string=new_password)
    pyperclip.copy(new_password)

# ---------------------------- PASSWORD SEARCH ------------------------------- #    

def search_password():
    website = website_entry.get()
    try:
        with open(f"{db_path}", "r") as data_file:
            data = json.load(data_file)
            entry = data[website]
    except FileNotFoundError:                
        messagebox.showinfo(message="Password not found")
    except KeyError:
        messagebox.showinfo(title=website, message="Password not found")
    else:
        messagebox.showinfo(title=website, message=f"username: {entry['username']}\npassword: {entry.get('password')}")
# ---------------------------- SAVE PASSWORD ------------------------------- #



def add_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    output = {
        website: {
            "username": username,
            "password": password
        }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(message="website is empty")
    else:
        is_ok = messagebox.askokcancel(message=f"are you happy with the following result:\n{output}", icon=messagebox.INFO)
        if is_ok:
            try:
                with open(f"{db_path}", "r") as data_file:
                    data = json.load(data_file)
                    data.update(output)
            except FileNotFoundError:                
                with open(f"{db_path}", "w") as data_file:
                    json.dump(output, data_file, indent=4)
            else:
                with open(f"{db_path}", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            website_entry.delete(first=0, last=END)
            password_entry.delete(first=0, last=END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
padlock_img = PhotoImage(file=logo_path)
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=(FONT_NAME, 25))
website_label.grid(column=0, row=1)

search_button = Button(text="Search", command=search_password)
search_button.grid(column=2, row=1)

username_label = Label(text="Email/Username:", font=(FONT_NAME, 25))
username_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=(FONT_NAME, 25))
password_label.grid(column=0, row=3)

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

username_entry = Entry(width=35)
username_entry.insert(END, "myemail@ggo.com")
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
