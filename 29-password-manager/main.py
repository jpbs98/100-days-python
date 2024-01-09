import random
import string
from tkinter import Tk, Label, Button, Entry, Text, Canvas, PhotoImage, messagebox
import pyperclip


def gen_pw():
    """
    Generate a random password consisting of letters, numbers, and symbols.

    Returns
    -------
    str
        The generated password.
    """
    letters = string.ascii_letters
    numbers = string.digits
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letter_list = [random.choice(letters) for _ in range(nr_letters)]
    symbol_list = [random.choice(symbols) for _ in range(nr_symbols)]
    number_list = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = letter_list + symbol_list + number_list

    random.shuffle(password_list)

    password = "".join(password_list)
    password_gen.insert(1.0, password)
    pyperclip.copy(password)


def save_pw():
    """
    Save the entered website, email/username, and password to a file.
    """
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_gen.get(1.0, "end-1c")

    # handle empty fields
    if not website or not email_username or not password:
        messagebox.showerror(
            title="Empty Fields", message="Please don't leave any fields empty!"
        )
        return

    # confirm details
    if messagebox.askokcancel(
        title=website,
        message=f"These are the details entered: \nEmail: {email_username}"
        f"\nPassword: {password}"
        f"\nIs it ok to save?",
    ):
        with open("data.txt", "a", encoding="utf-8") as f:
            f.write(f"{website} | {email_username} | {password}\n")
            website_entry.delete(0, "end")
            password_gen.delete(1.0, "end")
            website_entry.focus()


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


website_label = Label(text="Website:")
website_label.grid(row=1, column=0)


email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)


password_label = Label(text="Password:")
password_label.grid(row=3, column=0)


website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()


email_username_entry = Entry()
email_username_entry.insert(0, "default@email.com")
email_username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")


password_gen = Text(width=25, height=1)
password_gen.grid(row=3, column=1)

password_gen_button = Button(text="Generate Password", width=15, command=gen_pw)
password_gen_button.grid(row=3, column=2)


add_pw_button = Button(text="Add", width=25, command=save_pw)
add_pw_button.grid(row=4, column=1, columnspan=2, sticky="EW")


window.mainloop()
