from main import main
from tkinter import messagebox, Tk
from database import check_user, create_user


def register(username: str, password: str):
    if username and password:
        create_user(username, password)
        print('Registered successfully')
    else:
        messagebox.showerror(title='Registration', message='Invalid username or password')


def enter(username: str, password: str, root: Tk):
    if check_user(username, password):
        root.destroy()
        main()
    else:
        messagebox.showerror(title='Registration', message='User doesn\'t exist')