from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import time
from presenter.configuration import config

app = Flask(__name__)


app.config.update(config().as_dict())
db = SQLAlchemy(app)

from presenter.controllers.homepage import home_blueprint

app.register_blueprint(home_blueprint)

from presenter.controllers.movies import movies_blueprint

app.register_blueprint(movies_blueprint)

from presenter.controllers.new_movie import newmovie_blueprint

app.register_blueprint(newmovie_blueprint)

from presenter.controllers.actors import actors_blueprint

app.register_blueprint(actors_blueprint)
