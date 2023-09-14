from stegano import exifHeader


def encrypt(image, message):
    return exifHeader.hide(image, image, message)


def decrypt(image):
    message = exifHeader.reveal(image).decode()
    return message
