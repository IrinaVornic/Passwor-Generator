from tkinter import *
from tkinter import messagebox
import secrets
import string
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password(length=12):
    simbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    alphabet = string.ascii_letters + string.digits + ''.join(simbols)
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    password_entry.insert(0, password)
    pyperclip.copy(password)
    pyperclip.paste()
# ---------------------------- SAVE PASSWORD ------------------------------- #
# with open('all_passwords', 'w') as f:
#     f.write('My Passwords\n')


def save_info():
    website_info = wbsite_entry.get()
    email_info = mail_entry.get()
    password_info = password_entry.get()
    new_data = {
        website_info.title(): {
            'email': email_info,
            'password': password_info
        }
    }

    if len(website_info) == 0 or len(email_info) == 0 or len(password_info) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any field empty!")
    #
    # else:
    #     is_ok = messagebox.askokcancel(title=website_info, message=f"These are the details entered: \nEmail: "
    #                                                                f"{email_info} \nPassword: {password_info} "
    #                                                                f"\nIs it ok ti save?")
    #     if is_ok:
    else:
        try:
            with open('data.json', 'r') as data_file:
                # reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # updating old data with new data
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            wbsite_entry.delete(0, 'end')
            password_entry.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()


window.title('Password Manager')
window.config(padx=40, pady=50)
# Canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)
# Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)
email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)
password_label = Label(text='Password:', width=14)
password_label.grid(column=0, row=3)
# Entry
wbsite_entry = Entry(width=38)
wbsite_entry.grid(column=1, row=1, columnspan=2)
wbsite_entry.focus()
mail_entry = Entry(width=38)
mail_entry.grid(row=2, column=1, columnspan=2)
mail_entry.insert(END, string="irinavornic816@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)
# Buttons
pass_gen_btn = Button(text='Generate Password', command=generate_password)
pass_gen_btn.grid(column=2, row=3)
add_btn = Button(text='Add', width=36, command=save_info)
add_btn.grid(row=4, column=1, columnspan=2)
window.mainloop()
