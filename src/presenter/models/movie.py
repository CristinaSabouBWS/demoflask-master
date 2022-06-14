from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Index
from sqlalchemy.orm import relationship
from presenter.app import db
import datetime
from sqlalchemy.orm import validates
import ipdb


class Movie(db.Model):
    __tablename__ = "movies"
    id = Column(Integer, nullable=False, primary_key=True, unique=True)
    genre = Column(String(255))
    date_of_scraping = Column(String(12))
    directors = Column(String(255))
    title = Column(String(255), nullable=False)
    rating = Column(Integer)
    release_year = Column(Integer, nullable=True)
    top_cast = Column(String(300))
    url = Column(String(255), nullable=False)
    uid = Column(String(9), nullable=False)
    image_url = Column(String(250))
    image_path = Column(String(250))

    def __repr__(self):
        return "<Movie id=%s %r>" % (self.uid, self.title)

    @validates("uid")
    def validate_uid(self, key, uid):
        # ipdb.set_trace()
        # assert len(uid) > 2, "uid not valid"
        if not getattr(self, "errors", None):
            self.errors = []
        if len(uid) < 2:
            self.errors.append("uid is not valid")

        return uid
