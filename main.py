import os

from models.database import DATABASE_NAME
from models import create_database as db_creator

from register import register_form


def main():
    db_is_created = os.path.exists(DATABASE_NAME)

    if not db_is_created:
        db_creator.create_database()

    # register_form()


if __name__ == '__main__':
    main()