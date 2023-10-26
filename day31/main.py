from tkinter import *
from PIL import ImageTk, Image
import pandas as pd
import os
import random
current_directory = os.path.dirname(os.path.abspath(__file__))
images_directory = "images"
data_directory = "data"
timer = None
current_word = ""
words_to_learn_path = os.path.join(current_directory, data_directory, 'words_to_learn.csv')

BACKGROUND_COLOR = "#B1DDC6"
 
french_words = pd.read_csv(os.path.join(current_directory, data_directory, 'french_words.csv'))
french_dict = french_words.to_dict('records')

german_words = pd.read_csv(os.path.join(current_directory, data_directory, 'german-top-words.csv'))
german_dict = german_words.iloc[:, 1:].to_dict('records')

words_to_learn = None
if os.path.exists(words_to_learn_path):
    words_to_learn = pd.read_csv(words_to_learn_path).to_dict('records')
else:
    words_to_learn = german_dict #Change to french_dict for french


card_back = "card_back.png"
card_back_path = os.path.join(current_directory, images_directory, card_back)

card_front = "card_front.png"
card_front_path = os.path.join(current_directory, images_directory, card_front)

right = "right.png"
right_path = os.path.join(current_directory, images_directory, right)

wrong = "wrong.png"
wrong_path = os.path.join(current_directory, images_directory, wrong)

def prep_image(path, size):
    og = Image.open(path)
    resized = og.resize(size)
    img = ImageTk.PhotoImage(resized)
    return img

def change_word():
    global timer, current_word
    window.after_cancel(timer)
    current_word = random.choice(words_to_learn)
    canvas.itemconfig(card_image, image=card_front_img)
    canvas.itemconfig(title_text, fill="black", text=list(current_word.keys())[False])
    canvas.itemconfig(word_text, fill="black", text=list(current_word.values())[False])
    timer = window.after(3000, show_solution)

def show_solution():
    global current_word
    canvas.itemconfig(card_image, image=card_back_img)
    canvas.itemconfig(title_text, text=list(current_word.keys())[True], fill="white")
    canvas.itemconfig(word_text, text=list(current_word.values())[True], fill="white")

def learn_word():
    global current_word
    target = list(current_word.values())[True]
    new_list = [item for item in german_dict if target not in item.values()]
    df = pd.DataFrame(new_list)
    df.to_csv(words_to_learn_path, index=False)
    change_word()
   
window = Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

canvas = Canvas(width=600, height=400, background=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR)

card_back_img = prep_image(card_back_path, (500, 300))
card_front_img = prep_image(card_front_path, (500, 300))

card_image = canvas.create_image(300, 200, image=card_front_img)
title_text = canvas.create_text(300, 150, fill="black", text="Title", font=("Arial", 40, "italic"))
word_text = canvas.create_text(300, 220, fill="black", text="word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right_img = prep_image(right_path, (50,50))
right_button = Button(image=right_img, highlightbackground=BACKGROUND_COLOR, command=learn_word)
right_button.grid(column=0, row=1)

wrong_img = prep_image(wrong_path, (50,50))
wrong_button = Button(image=wrong_img, highlightbackground=BACKGROUND_COLOR, command=change_word)
wrong_button.grid(column=1, row=1)

timer = window.after(3000, show_solution)
change_word()

window.mainloop()
