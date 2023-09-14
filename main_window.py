from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

from encrypt import encrypt, decrypt


def open_file():
    filename = filedialog.askopenfilename(initialdir='C:',
                                      title='Select image',
                                      filetypes=(('JPG files', '*.jpg'), ('PNG files', '*.png'), ('All files', '*.*')))

    return filename


def encrypt_image(message):
    filename = open_file()

    encrypt(filename, message)


def decrypt_image():
    filename = open_file()

    message = decrypt(filename)
    return message


def create_main_window():
    root = Tk()
    root.title('Cryptographer')
    root.iconbitmap('static/icon/favicon.ico')
    root.geometry('1024x600')
    root.resizable(False, False)

    background_image = ImageTk.PhotoImage(Image.open('static/images/background1.jpg'))
    Label(root, image=background_image).place(x=-2, y=0)



    root.mainloop()


if __name__ == '__main__':
    create_main_window()

