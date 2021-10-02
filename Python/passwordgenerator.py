import pyperclip
import random
import csv
import os
from tkinter import *
from tkinter.ttk import *

# Function for calculation of password
def low():
    entry.delete(0, END)
    # Get the length of passowrd
    length = var1.get()
    words = var2.get()
    words_without_space = words.replace(" ", "")
    digits = "0123456789"
    special = "!@#$%^&*()"
    password = ""
    if words_without_space == "":
        return "Error: Please enter some words."
    else:
        # for strong password
        for i in range(0, length-2):
            password = password + random.choice(words_without_space)
        password = password + random.choice(digits)
        password = password + random.choice(special)
        with open('passwords.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            words = words + str(length)
            writer.writerow([words, password])
        file.close()
        return password

# Function for generation of password
def generate():
    password1 = low()
    entry.insert(10, password1)

# Function for copying password to clipboard
def remember():
    entry.delete(0, END)
    data = []
    with open("passwords.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    length = var1.get()
    words = var2.get()
    words = words + str(length)
    col = [x[0] for x in data]
    if words in col:
        for x in range(0, len(data)):
            if words == data[x][0]:
                entry.insert(10, data[x][1])
    else:
        entry.insert(10, "Words not entered before in this order.")

# Main Function
# clear file data
f = open("passwords.csv", "w")
f.truncate()
f.close()

# create GUI window
root = Tk()
root.geometry('410x50')
var = IntVar()
var1 = IntVar()
var2 = StringVar()

# Title of your GUI window
root.title("Random Password Generator")

# create label and entry to show password generated
Random_password = Label(root, text="Password")
Random_password.grid(row=1, column=2)
entry = Entry(root)
entry.grid(row=1, column=3, ipadx=10)

# create label for length of password
c_label = Label(root, text="Length")
c_label.grid(row=1)

# create Buttons Copy which will copy password to clipboard and Generate which will generate the password
generate_button = Button(root, text="Generate", command=generate)
generate_button.grid(row=0, column=2)
copy_button = Button(root, text="Remember", command=remember)
copy_button.grid(row=0, column=3)

# Create label and entry for words from user
radio_strong = Label(root, text="Words")
radio_strong.grid(row=0)
enter = Entry(root, textvariable=var2)
enter.grid(row=0, column=1, ipadx=8)

combo = Combobox(root, textvariable=var1)

# Combo Box for length of your password
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
                   17, 18, 19, 20, 21, 22, 23, 24, 25,
                   26, 27, 28, 29, 30, 31, 32, "Length")
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1, row=1)

# start the GUI
root.mainloop()
