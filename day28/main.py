from tkinter import *
import os
current_directory = os.path.dirname(os.path.abspath(__file__))
file_name = "./tomato.png"
file_path = os.path.join(current_directory, file_name)

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
FONT_BOLD = "bold"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=file_path)
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 112, fill="white", text="00:00", font=(FONT_NAME, 35, FONT_BOLD))
canvas.pack()

window.mainloop()