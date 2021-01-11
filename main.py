from tkinter import *
import random
import string

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
url_input = Entry(width=35, bd=3)
url_input.grid(column=1, row=1, columnspan=2, padx=(8, 5), pady=(5, 5))
url_input.focus()
url = url_input.get()

username_label = Label(text='Username/Email', font=(FONT_NAME,
                                                    18, 'normal'), bg=DARK_BG, fg=WHITE, highlightthickness=0)
username_label.grid(column=0, row=2)
username_input = Entry(width=20, bd=3)
username_input.grid(column=1, row=2, padx=(5, 5), pady=(5, 5))
username_input.insert(0, EMAIL)

pass_label = Label(text='Password', font=(
    FONT_NAME, 18, 'normal'), bg=DARK_BG, fg=WHITE, highlightthickness=0)
pass_label.grid(column=0, row=3)
pass_input = Entry(width=20, bd=3)
pass_input.grid(column=1, row=3, padx=(5, 5), pady=(5, 5))


def generate_pass():
    """inputs a random password into password field on command"""
    password = random_password()
    pass_input.insert(0, password)


# -------------- save url, username, password to csv file ------------ #
filename = "./safe_pass.txt"

with open(filename, 'w') as f:
    f.write("URL" + " || " + "USERNAME" + " || " + "PASSWORD" + "\n")


def save_info():
    """Retreive user inputs for url, username, password and save to file"""
    with open(filename, 'a') as f:
        url = url_input.get()
        username = username_input.get()
        password = pass_input.get()
        f.write(url + " || " + username + " || " + password + "\n")
        url_input.delete(0, END)
        username_input.delete(0, END)
        username_input.insert(0, EMAIL)
        pass_input.delete(0, END)


# generate password button
pass_generator = Button(text="Generate Password", command=generate_pass)
pass_generator.grid(column=2, row=3, padx=(5, 5))

# save button, save input data into file on command
save_button = Button(text='Save', command=save_info, width=20)
save_button.grid(column=1, row=4, pady=(5, 5))


window.mainloop()
