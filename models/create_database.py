from models.database import create_db, Session
from models.user import User


def create_database():
    create_db()


def check_user(username: str, password: str) -> bool:
    return

    if username in temp_database.keys():
        password_hash = hash(password)

        if temp_database[username] == password_hash:
            print('Welcome')
            return True

    print(temp_database)
    print('Error')
    return False


def create_user(username: str, password: str) -> None:
    session = Session()

    user = User(name=username, password_hash=hash(password))
    session.add(user)

    session.commit()
    session.close()

    print('User created successfully')


