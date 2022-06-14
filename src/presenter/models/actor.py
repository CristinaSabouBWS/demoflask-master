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

    @validates("uid")
    def validate_uid(self, key, uid):
        # ipdb.set_trace()
        # assert len(uid) > 2, "uid not valid"
        if not getattr(self, "errors", None):
            self.errors = []
        if len(uid) < 2:
            self.errors.append("uid is not valid")

        return uid
