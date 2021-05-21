from sqlalchemy import Column, String, Integer, Boolean, DateTime
from flask_login import UserMixin
from blog.models.database import db
from datetime import datetime


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    user_name = Column(String(80), unique=True, nullable=False)
    email = Column(String(128), unique=True, nullable=False)
    pswd_hash = Column(String(128))
    reg_date = Column(DateTime, unique=True, nullable=False, default=None)
    update = Column(DateTime, nullable=False)
    first_name = Column(String(80))
    last_name = Column(String(128))

    def __init__(self, username, email, firstname=None, lastname=None, pswd=None, regdate=None):
        self.user_name = username
        self.email = email
        if regdate is None:
            regdate = datetime.utcnow()
            self.reg_date = regdate
        self.update = datetime.utcnow()
        self.first_name=firstname
        self.last_name=lastname

    def __repr__(self) -> str:
        return f'User("{self.user_name}", "{self.email}")'

    def __str__(self) -> str:
        s = f'Пользователь {self.user_name}, Email: {self.email}, зарегистрировался {self.reg_date}.'
        if self.first_name:
            s += f'\nИмя: {self.first_name}, '
        if self.last_name:
            s += f'Фамилия: {self.last_name}.'
        return s

