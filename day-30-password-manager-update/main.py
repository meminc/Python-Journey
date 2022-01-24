from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

PADDING = 5


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        # Reading data
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="File Not Found Error", message="No Data File Found")
    else:
        try:
            email = data[website]["email"]
            password = data[website]["password"]
        except KeyError:
            messagebox.showerror(title="Key Error", message="No details for the website exists")
        else:
            pyperclip.copy(password)
            messagebox.showinfo(title="Details were founded", message=f"email: {email}\n"
                                                                      f"password: {password}")
    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:  # -> will be triggered everything inside try run
            # Updating old data with net data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updating data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(bg="white", padx=50, pady=50)

canvas = Canvas(bg="white", height=200, width=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(bg="white", text="Website:")
website_label.grid(row=1, column=0, sticky="E", padx=PADDING, pady=PADDING)
email_label = Label(bg="white", text="Email/Username:")
email_label.grid(row=2, column=0, sticky="E", padx=PADDING, pady=PADDING)
password_label = Label(bg="white", text="Password:")
password_label.grid(row=3, column=0, sticky="E", padx=PADDING, pady=PADDING)

# Entries
website_entry = Entry(width=30)
website_entry.grid(row=1, column=1, sticky="W", padx=PADDING, pady=PADDING)
website_entry.focus()
email_entry = Entry(width=55)
email_entry.grid(row=2, column=1, columnspan=2, sticky="W", padx=PADDING, pady=PADDING)
email_entry.insert(0, "muhammetemincinalioglu@gmail.com")
password_entry = Entry(width=30)
password_entry.grid(row=3, column=1, sticky="W", padx=PADDING, pady=PADDING)

# Buttons
search_button = Button(text="Search", bg="white", width=18, command=find_password)
search_button.grid(row=1, column=2, sticky="E", padx=PADDING, pady=PADDING)
generate_password_button = Button(text="Generate Password", bg="white", width=18, command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="E", padx=PADDING, pady=PADDING)
add_button = Button(text="Add", bg="white", width=18, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="E", padx=PADDING, pady=PADDING)

window.mainloop()
