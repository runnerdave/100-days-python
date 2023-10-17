import math
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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def stop_timer():
    global reps
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    blocks_label.config(text="")
    reps = 0
    start_button.config(state="normal")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_time():
    start_button.config(state="disabled")
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    global reps
    reps += 1
    if reps % 2 != 0:
        count_down(work_sec)
        timer_label.config(text="Work", fg=RED)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long break", fg=GREEN)
    else:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = str(count % 60).zfill(2)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_time()
        checks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            checks += "✓ "
        blocks_label.config(text=checks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=file_path)
canvas.create_image(100, 112, image=tomato_img)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
timer_label.grid(column=1, row=0)

timer_text = canvas.create_text(100, 112, fill="white", text="00:00", font=(FONT_NAME, 35, FONT_BOLD))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", bg=YELLOW, command=start_time, highlightbackground=YELLOW, highlightcolor=YELLOW)
start_button.grid(column=0, row=2)

stop_button = Button(text="Reset", bg=YELLOW, command=stop_timer, highlightbackground=YELLOW, highlightcolor=YELLOW)
stop_button.grid(column=2, row=2)

blocks_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, FONT_BOLD))
blocks_label.grid(column=1, row=3)


window.mainloop()