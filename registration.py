from main_window import create_main_window
from tkinter import messagebox, Tk
from models.create_database import check_user, create_user


def register(username: str, password: str):
    if username and password:
        create_user(username, password)
    else:
        messagebox.showerror(title='Registration', message='Invalid username or password')


def enter(username: str, password: str, root: Tk):
    if check_user(username, password):
        root.destroy()
        create_main_window()
    else:
        messagebox.showerror(title='Registration', message='User doesn\'t exist')