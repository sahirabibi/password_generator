from tkinter import *
from tkinter import messagebox
import random
import string
import json

DARK_BG = "#000D30"
LIGHT_BG = "#BACBFB"
DARK_THEME = "./darktheme.png"
LIGHT_THEME = "./lighttheme.png"
FONT_NAME = "Courier"
WHITE = "#FCFCFC"
EMAIL = "placeholder@email.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# function to generate a random password for user

# list of characters to be used:
lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
symbols = ['!', '@', '#', '&']
numbers = [str(i) for i in range(1, 10)]


def random_password():
    """Returns a random 8-char password of uppercase, lowercase, numbers, and symbols"""
    password = []
    for i in range(2):
        password.append(random.choice(lower))
        password.append(random.choice(upper))
        password.append(random.choice(symbols))
        password.append(random.choice(numbers))
    random.shuffle(password)
    return "".join(password)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("SafePass")
window.config(padx=30, pady=30, bg=DARK_BG)


# insert selected background (Dark/Light)
canvas = Canvas(width=250, height=250, bg=DARK_BG, highlightthickness=0)
photo = PhotoImage(file=DARK_THEME)
canvas.create_image(125, 125, image=photo)
canvas.grid(column=1, row=0)


# labels and input boxes for url, username, passwords

url_label = Label(text='URL', font=(FONT_NAME, 18, 'normal'),
                  bg=DARK_BG, fg=WHITE, highlightthickness=0)
url_label.grid(column=0, row=1)
url_input = Entry(width=20, bd=0)
url_input.grid(column=1, row=1,)
url_input.focus()
url = url_input.get()

username_label = Label(text='Username/Email', font=(FONT_NAME,
                                                    18, 'normal'), bg=DARK_BG, fg=WHITE, highlightthickness=0)
username_label.grid(column=0, row=2)
username_input = Entry(width=20, bd=0)
username_input.grid(column=1, row=2, padx=(5, 5), pady=(5, 5))
username_input.insert(0, EMAIL)

pass_label = Label(text='Password', font=(
    FONT_NAME, 18, 'normal'), bg=DARK_BG, fg=WHITE, highlightthickness=0)
pass_label.grid(column=0, row=3)
pass_input = Entry(width=20, bd=0)
pass_input.grid(column=1, row=3, padx=(5, 5), pady=(5, 5))


def generate_pass():
    """inputs a random password into password field on command"""
    password = random_password()
    pass_input.insert(0, password)


# -------------- save url, username, password to csv file, search ------------ #
filename = "./safe_pass.json"


def search():
    try:
        with open(filename, "r") as data_file:
            # load json data file
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(
            title="Error", message="No data file found.\nTry saving new login information and trying again.")
    else:
            # get the url
            url = url_input.get()
            if url in data:
                # get url values from dict
                info = data[url]
                username = info['username']
                password = info['password']
                # print values in messagebox for user
                messagebox.askokcancel(
                    title="Saved Password", message=f"Here is the saved information on file for {url}:\nUsername: {username}\nPassword: {password}")
            else:
                 messagebox.showwarning(
            title="Error", message="Information not on file. Please check your entry and try again!")
      
    


def save_info():
    """Retreive user inputs for url, username, password and save to file"""
    url = url_input.get()
    username = username_input.get()
    password = pass_input.get()
    new_data = {url:
                {
                    "username": username,
                    "password": password
                }}

    if len(url) == 0 or len(password) == 0:
        messagebox.showwarning(
            title="Error", message="You cannot leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(
            title=url, message=f"You entered:\nUsername:{username}\nPassword: {password}\nContinue to save?")
        if is_ok:
            try:
                with open(filename, "r") as data_file:
                    # reading old data
                    data = json.load(data_file)
                    # updating old data with new data
                    data.update(new_data)
                with open(filename, "w") as data_file:
                    json.dump(data, data_file, indent=4)
            except FileNotFoundError:
                with open(filename, "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            finally:
                url_input.delete(0, END)
                pass_input.delete(0, END)


# generate password button
pass_generator = Button(text="Generate Password",
                        width=20, command=generate_pass)
pass_generator.grid(column=2, row=3)

# save button, save input data into file on command
save_button = Button(text="Save", width=20, command=save_info, )
save_button.grid(column=1, row=4, pady=(5, 5))

search_button = Button(text="Search", command=search, width=20)
search_button.grid(column=2, row=1)

window.mainloop()
