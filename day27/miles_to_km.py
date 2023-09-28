import tkinter as tk

window = tk.Tk()
window.config(padx=20, pady=20)


def calculate():
    value_label["text"] = round(float(miles_input.get())*1.609, 2)


window.title("Mile to Km Converter")
window.minsize(width=500, height=300)

miles_input = tk.Entry(width=10)
miles_input.insert(0, string="0")
miles_input.grid(column=1, row=0)

miles_label = tk.Label(text="Miles", font=("Arial", 24, "bold"))
miles_label.grid(column=2, row=0)

is_equal_label = tk.Label(text="is equal to", font=("Arial", 24, "bold"))
is_equal_label.grid(column=0, row=1)

value_label = tk.Label(text="0", font=("Arial", 24, "bold"))
value_label.grid(column=1, row=1)

km_label = tk.Label(text="Km", font=("Arial", 24, "bold"))
km_label.grid(column=2, row=1)

calculate_button = tk.Button(text="calculate", command=calculate)
calculate_button.grid(column=1, row=2)


window.mainloop()
