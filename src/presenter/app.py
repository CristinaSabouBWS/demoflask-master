from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import time
from presenter.configuration import config

UPLOAD_FOLDER = "/tmp"
ALLOWED_EXTENSIONS = {"json"}

app = Flask(__name__)

app.config.update(config().as_dict())
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["SECRET_KEY"] = "HaHA($(#$$33--"

app.config.update(config().as_dict())
db = SQLAlchemy(app)

from presenter.controllers.homepage import home_blueprint

app.register_blueprint(home_blueprint)

from presenter.controllers.movies import movies_blueprint

app.register_blueprint(movies_blueprint)


from presenter.controllers.actors import actors_blueprint

app.register_blueprint(actors_blueprint)

from presenter.services.search import search_blueprint

app.register_blueprint(search_blueprint)
