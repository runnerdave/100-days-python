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

def start_timer():
    pass

def stop_timer():
    pass

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=file_path)
canvas.create_image(100, 112, image=tomato_img)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
timer_label.grid(column=1, row=0)

canvas.create_text(100, 112, fill="white", text="00:00", font=(FONT_NAME, 35, FONT_BOLD))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", bg=YELLOW, command=start_timer, highlightbackground=YELLOW, highlightcolor=YELLOW)
start_button.grid(column=0, row=2)

stop_button = Button(text="Stop", bg=YELLOW, command=stop_timer, highlightbackground=YELLOW, highlightcolor=YELLOW)
stop_button.grid(column=2, row=2)

blocks_label = Label(text="✓", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, FONT_BOLD))
blocks_label.grid(column=1, row=3)


window.mainloop()