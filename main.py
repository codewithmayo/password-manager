from tkinter import *
from tkinter import messagebox
import random
import json


# ------------------------------FIND PASSWORD-------------------------------------#
def find_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found")
        website = website_name_entry.get()
        email = data[website]['email']
        password = data[website]['password']
        if website in data and len(website) != 0:
            messagebox.showinfo(title=website, message=f"Email: {email} Password: {password}")
        else:
            messagebox.showerror(title="Error", message="No data found,")
# todo: fix the above else statement code is correct but need to check documentation


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)


def generate_password():
    password_entry.delete(0, END)
    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website_name = website_name_entry.get()
    my_email = email_entry.get()
    password_text = password_entry.get()
    new_data = {
        website_name: {
            "email": my_email,
            "password": password_text
        }
    }

    if len(website_name) == 0 or len(my_email) == 0 or len(password_text) == 0:
        messagebox.showerror(title="Error", message="You left some fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
        finally:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
                website_name_entry.delete(0, "end")
                password_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# setting up image
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# labels
website_name_label = Label(text="Website name:")
website_name_label.grid(column=0, row=1)

email_label = Label(text="Email:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# entries
website_name_entry = Entry(width=35)
website_name_entry.grid(column=1, row=1)
website_name_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(END, "qamarkhan3120@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# buttons
find_password_button = Button(text="Search", highlightthickness=0, command=find_password)
find_password_button.grid(column=2, row=1)

generate_password_button = Button(text="Generate password", highlightthickness=0, command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, highlightthickness=0, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)
window.mainloop()
