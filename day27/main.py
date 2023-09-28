import tkinter as tk

window= tk.Tk()

window.title("My First GUI")
window.minsize(width=500, height=300)

label = tk.Label(text="I am a label", font=("Arial", 24, "bold"))
label.grid(column=0, row=0)

label["text"] = "New text"
label.config(text="Newer text")

def button_clicked():
    print("clicked")
    label["text"] = entry.get()

button= tk.Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

new_button= tk.Button(text="new button", command=button_clicked)
new_button.grid(column=2, row=0)

entry = tk.Entry(width=10)
entry.grid(column=3, row=2)

window.mainloop()