import json
from tkinter import *
from tkinter import messagebox
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def calculate():
    a = websiteinput.get()
    key = keyinput.get()
    if len(a) == 0 or key == 0:
        messagebox.showinfo(title="OOPS", message="You have left either the website or key field Empty")
    else:
        end_text = ""
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u',
                    'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                    'p',
                    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for letter in a.lower():

            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position + int(key)
                end_text += alphabet[new_position]

        end_text_2 = ""
        if int(key) % 2 == 0:
            for letter in end_text:
                index = end_text.index(letter)

                if index % 2 == 0:
                    letter = letter.upper()
                end_text_2 += letter
        else:
            for letter in end_text:
                index = end_text.index(letter)

                if index % 2 != 0:
                    letter = letter.upper()
                end_text_2 += letter

        passshow.insert(0, end_text_2)
        pyperclip.copy(end_text_2)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = websiteinput.get()
    password = passshow.get()
    key = keyinput.get()
    new_data = {
        website: {
            "Password": password
        }
    }

    if len(website) == 0 or key == 0:
        messagebox.showinfo(title="OOPS", message="You have left either the website or key field Empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            websiteinput.delete(0, END)
            keyinput.delete(0, END)
            passshow.delete(0, END)
            messagebox.showinfo(title="Final", message="It is Saved")

#---------------------------Search PAssword-----------------------------#

def findpassword():
    website = websiteinput.get().lower()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except:
        messagebox.showinfo(title="Error",message="NO DATA FOUND")
    else:
        if website in data:
            password = data[website]["Password"]
            messagebox.showinfo(title="Hello",message=f"Your Password for {website} is:  {password}")
            pyperclip.copy(password)
        else:
            messagebox.showinfo(title="Error",message="No password for the Website foundd")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("My Password")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

# ------------------Label_____________________
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="KEY:")
email_label.grid(row=2, column=0)

pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

# ---------------------Entry--------------------------

websiteinput = Entry(width=21)
websiteinput.grid(row=1, column=1)
websiteinput.focus()

keyinput = Entry(width=39)
keyinput.grid(row=2, column=1, columnspan=2)

passshow = Entry(width=21)
passshow.grid(row=3, column=1)

# -------------------------Button-----------------

searchbutton = Button(text="Search",width=13,command=findpassword)
searchbutton.grid(row=1,column=2)

tellpassbutton = Button(text="Show Password", width=14, command=calculate)
tellpassbutton.grid(row=3, column=2)

add_button = Button(text="Add in List", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
