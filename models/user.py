#!/usr/bin/python3
""" holds class User"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Representation of a user """
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
        if 'password' in kwargs:
            self.password = kwargs['password']

    @property
    def password(self):
        """Get the password"""
        return self._password

    @password.setter
    def password(self, value):
        """Set the password, hashing it with MD5"""
        self._password = md5(value.encode()).hexdigest()

    def to_dict(self, include_password=False):
        """Override the to_dict method to exclude the password by default"""
        dict_representation = super().to_dict(include_password)
        if 'password' in dict_representation and not include_password:
            del dict_representation['password']
        return dict_representation
