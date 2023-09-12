from tkinter import *
from PIL import ImageTk, Image

from registration import register, enter


def register_form():
    # configuration
    root = Tk()
    root.title('Cryptographer')
    root.geometry('612x400')
    root.resizable(False, False)
    root['bg'] = 'black'
    root.iconbitmap('static/icon/favicon.ico')

    # set background
    background_image = ImageTk.PhotoImage(Image.open('static/images/background1.jpg'))
    Label(root, image=background_image).place(x=-2, y=0)

    # creation of register form
    form = Frame(root, width=500, height=300, bg='#061733', relief=SUNKEN, padx=20, pady=20)
    form.pack(padx=100, pady=120)

    username = StringVar()
    Label(form, text='Username', bg='#061733', fg='#eef', font=32).grid(row=0, column=0, sticky=W, padx=10,
                                                                        pady=5)
    Entry(form, textvariable=username, bg='#0270B8', fg='#eef').grid(row=0, column=1, padx=10, pady=10)

    password = StringVar()
    Label(form, text='Password', bg='#061733', fg='#eef', font=32).grid(row=1, column=0, sticky=W, padx=10,
                                                                        pady=5)
    Entry(form, textvariable=password, show='*', bg='#0270B8', fg='#eef').grid(row=1, column=1, padx=10,
                                                                               pady=10)

    Button(form, text='Register', bg='#1C84B8', fg='#061733',
           command=lambda: register(username.get(), password.get())).grid(row=2, column=0,
                                                                          sticky=W,
                                                                          pady=25,
                                                                          padx=10)
    Button(form, text='Enter', bg='#1C84B8', fg='#061733',
           command=lambda: enter(username.get(), password.get(), root)).grid(row=2, column=1, sticky=E, pady=25, padx=10)

    root.mainloop()


if __name__ == '__main__':
    register_form()
