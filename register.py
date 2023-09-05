from tkinter import *
from PIL import ImageTk, Image


# Configuration
root = Tk()
root.title('Cryptographer')
root.geometry('612x400')
root['bg'] = 'black'
root.iconbitmap('static/icon/favicon.ico')

background_image = ImageTk.PhotoImage(Image.open('static/images/background1.jpg'))
Label(root, image=background_image).place(x=-2, y=0)


form = Frame(root, width=500, height=300, bg='#eeffcc', relief=SUNKEN)
form.pack(padx=100, pady=120)


login = StringVar()
login_label = Label(form, text='Login').grid(row=0, column=0)
login_entry = Entry(form, textvariable=login).grid(row=0, column=1)

password = StringVar()
password_label = Label(form, text='Password').grid(row=1, column=0)
password_entry = Entry(form, textvariable=password, show='*').grid(row=1, column=1)

registration_button = Button(form, text='Register').grid(row=2, column=0, sticky=W, pady=10, padx=10)
enter_button = Button(form, text='Enter').grid(row=2, column=1, sticky=E, pady=10, padx=10)


root.mainloop()
