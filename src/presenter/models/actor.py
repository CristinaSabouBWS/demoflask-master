from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Index
from sqlalchemy.orm import relationship
from presenter.app import db
from sqlalchemy.orm import validates
import ipdb


class Actor(db.Model):
    __tablename__ = "actors"
    id = Column(Integer, nullable=False, primary_key=True, unique=True)
    name = Column(String(255), nullable=False)
    uid = Column(String(10), nullable=False)
    filmography_movie_url = Column(String(500))
    filmography_movie_title = Column(String(500))

    def __repr__(self):
        return "<Actor id=%s %r>" % (self.id, self.name)

    @validates("uid", "name")
    def validate_fields(self, keys, values):
        if keys == "uid":
            assert values != "", "uid is not valid"
        if keys == "name":
            assert values != "", "name is not valid"
        return values
