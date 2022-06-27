from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Index
from sqlalchemy.orm import relationship
from presenter.app import db
from sqlalchemy.orm import validates
import ipdb
import re


class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, nullable=False, primary_key=True, unique=True)
    name = Column(String(255), nullable=False)
    email = Column(String(200), nullable=False, unique=True)
    password = Column(String(200), nullable=False)

    def __repr__(self):
        return "<User id=%s %r>" % (self.id, self.name)

    # @validates("email", "name", "password")
    # def validate_fields(self, key, values):
    #     pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    #     if key == "email":
    #     #     assert re.match(pat, values), "email is not valid"
    #     if key == "email":
    #         assert values != "", "email can not be blank"
    #     if key == "name":
    #         assert values != "", "name can not be blank"
    #     return values
