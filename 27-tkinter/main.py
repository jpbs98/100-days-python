from tkinter import Tk, Label, Button, Entry


def calculate():
    miles = float(miles_input.get())
    km = round(miles * 1.609, 2)
    km_out.config(text=km)


window = Tk()
window.title("Miles to Km Converter")
window.maxsize(width=300, height=300)
window.config(padx=20, pady=20)

# labels
miles_label = Label(text="Miles")
km_label = Label(text="Km")
miles_label.grid(column=2, row=0)
km_label.grid(column=2, row=1)

# miles entry
miles_input = Entry(width=10, justify="center")
miles_input.grid(column=1, row=0)
miles_input.focus()

# km output
km_out = Label(text="0", width=10)
km_out.grid(column=1, row=1)

# equal to text
equal_to_text = Label(text="is equal to")
equal_to_text.grid(column=0, row=1)

# calculate button
calc_button = Button(text="Calculate", command=calculate)
calc_button.grid(column=1, row=2)


window.mainloop()
