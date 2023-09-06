temp_database = {
    'admin': hash('1234'),
    'user': hash('qwerty'),
}


def check_user(username: str, password: str) -> bool:
    if username in temp_database.keys():
        password_hash = hash(password)

        if temp_database[username] == password_hash:
            print('Welcome')
            return True

    print(temp_database)
    print('Error')
    return False


def create_user(username: str, password: str) -> None:
    temp_database[username] = hash(password)
    print('User created successfully')
