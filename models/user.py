from sqlalchemy import Column, String, Integer
from models.database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password_hash = Column(Integer)

    def __init__(self, name, password_hash):
        self.name = name
        self.password_hash = password_hash

    def __repr__(self):
        return f'{self.name}: {self.password_hash}'
