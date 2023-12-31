from models.database import create_db, Session
from models.user import User
from hash_function import hashf


def create_database():
    create_db()


def check_user(username: str, password: str) -> bool:
    session = Session()
    all_users = session.query(User)
    session.close()

    for user in all_users:
        if (username == user.name) and (hashf(password) == user.password_hash):
            return True

    return False


def create_user(username: str, password: str) -> None:
    session = Session()

    user = User(name=username, password_hash=hashf(password))
    session.add(user)

    session.commit()
    session.close()

    print('User created successfully')
