from tkinter import *
from PIL import ImageTk, Image


# Configuration
root = Tk()
root.title('Cryptographer')
root.geometry('612x400')
root.resizable(False, False)
root['bg'] = 'black'
root.iconbitmap('static/icon/favicon.ico')

background_image = ImageTk.PhotoImage(Image.open('static/images/background1.jpg'))
Label(root, image=background_image).place(x=-2, y=0)


form = Frame(root, width=500, height=300, bg='#061733', relief=SUNKEN, padx=20, pady=20)
form.pack(padx=100, pady=120)


login = StringVar()
login_label = Label(form, text='Login', bg='#061733', fg='#eef', font=32).grid(row=0, column=0, sticky=W, padx=10, pady=5)
login_entry = Entry(form, textvariable=login, bg='#0270B8', fg='#eef').grid(row=0, column=1, padx=10, pady=10)

password = StringVar()
password_label = Label(form, text='Password', bg='#061733', fg='#eef', font=32).grid(row=1, column=0, sticky=W, padx=10, pady=5)
password_entry = Entry(form, textvariable=password, show='*', bg='#0270B8', fg='#eef').grid(row=1, column=1, padx=10, pady=10)


registration_button = Button(form, text='Register', bg='#1C84B8', fg='#061733').grid(row=2, column=0, sticky=W, pady=20, padx=10)
enter_button = Button(form, text='Enter', bg='#1C84B8', fg='#061733').grid(row=2, column=1, sticky=E, pady=20, padx=10)


root.mainloop()
