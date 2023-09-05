temp_database = {
    'admin': hash('1234'),
    'user': hash('qwerty'),
}


def check_user(login: str, password: str) -> bool:
    if login in temp_database.keys():
        password_hash = hash(password)

        if temp_database[login] != password_hash:
            print('Error')
            return False
        else:
            print('Welcome')
            return True

    return False

