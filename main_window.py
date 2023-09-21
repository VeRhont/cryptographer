from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

from encrypt import encrypt, decrypt


def open_file():
    filename = filedialog.askopenfilename(initialdir='C:',
                                          title='Select image',
                                          filetypes=(
                                              ('JPG files', '*.jpg'), ('PNG files', '*.png'), ('All files', '*.*')))

    return filename


def encrypt_image(root, message):
    filename = open_file()
    encrypt(filename, message)

    root.destroy()
    create_main_window()


def decrypt_image():
    filename = open_file()

    message = decrypt(filename)
    return message


def create_encrypt_ui(root, form):
    form.destroy()

    label = Label(root, text='Enter message you want to encrypt:', bg='#061733', fg='#eef', font=32)
    entry = Entry(root, width=100)
    button = Button(root, text='Choose file', bg='#1C84B8', fg='#061733', font=10, command=lambda: encrypt_image(root, entry.get()))

    label.pack(padx=20, pady=20)
    entry.pack(padx=20, pady=10)
    button.pack(padx=40, pady=40)


def create_decrypt_ui(root, form):
    try:
        form.destroy()
        message = decrypt_image()
    except:
        message = 'No secret message'

    def update_form():
        root.destroy()
        create_main_window()

    label = Label(root, text='\n'.join(i for i in message.split())).pack(pady=20, padx=20)
    back = Button(root, text='BACK', bg='#1C84B8', fg='#061733', font=10, command=update_form).pack(pady=30, padx=20)


def create_main_ui(root):
    form = Frame(root, width=500, height=300, bg='#061733', relief=SUNKEN, padx=20, pady=20)
    form.pack(padx=300, pady=180)

    Label(form, text='Choose option:', bg='#061733', fg='#eef', font=32).pack(padx=20, pady=20)
    Button(form, text='ENCRYPT', bg='#1C84B8', fg='#061733', font=10, command=lambda: create_encrypt_ui(root, form)).pack(
        padx=100, pady=10)
    Button(form, text='DECRYPT', bg='#1C84B8', fg='#061733', font=10,
           command=lambda: create_decrypt_ui(root, form)).pack(padx=100, pady=10)


def create_main_window():
    root = Tk()
    root.title('Cryptographer')
    root.iconbitmap('static/icon/favicon.ico')
    root.geometry('1024x600')
    root.resizable(False, False)

    background_image = ImageTk.PhotoImage(Image.open('static/images/background1.jpg'))
    Label(root, image=background_image).place(x=-2, y=0)

    create_main_ui(root)

    root.mainloop()


if __name__ == '__main__':
    create_main_window()
