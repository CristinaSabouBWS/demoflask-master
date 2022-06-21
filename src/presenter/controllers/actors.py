from flask import Flask, Blueprint, jsonify, render_template, url_for, request, redirect, flash
from werkzeug.utils import secure_filename
import os

actors_blueprint = Blueprint("actors", __name__)

from presenter.app import app, db
from presenter.models.actor import Actor
import ipdb
import json
from presenter.app import app, db, ALLOWED_EXTENSIONS, UPLOAD_FOLDER


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@actors_blueprint.route("/actors/")
def index():
    all_actors = Actor.query.order_by(Actor.id).all()
    per_page = request.args.get("items", 5, type=int)
    current_page = request.args.get("page", 1, type=int)

    actors_count = len(all_actors)

    start = per_page * (current_page - 1)
    end = min(start + per_page, actors_count)
    actors = all_actors[start:end]
    error = ""
    if len(actors) == 0:
        error = "Error message, no more items"

    return render_template(
        "actors/index.html", actors=actors, current_page=current_page, items_per_page=per_page, error=error
    )


def to_list(dbstring):
    dbstring = dbstring.strip("][")
    li = dbstring.split(", ")
    result = []
    for item in li:
        result.append((item[1:-1]))
    return result


@actors_blueprint.route("/actors/<id>")
def show(id):
    item = Actor.query.get(id)
    filmography_name = item.filmography_movie_title
    filmography_url = item.filmography_movie_url
    filmography = [x for x in zip(to_list(filmography_name), to_list(filmography_url))]
    return render_template("/actors/actor.html", actor={"name": item.name, "filmography": filmography, "id": item.id})


@actors_blueprint.route("/actors/new")
def new():
    return render_template("actors/new.html")


@actors_blueprint.route("/actors/new", methods=["POST"])
def create():
    try:
        actor = Actor(
            name=request.form.get("name"),
            uid=request.form.get("uid"),
            filmography_movie_url=request.form.get("filmography_movie_url"),
            filmography_movie_title=request.form.get("filmography_movie_title"),
        )

        db.session.add(actor)
        db.session.commit()
    except AssertionError as errors:
        return render_template("/actors/new.html", errors=errors)

    return redirect("/actors")


@actors_blueprint.route("/actors/<id>/edit")
def edit(id):
    query = Actor.query.filter_by(id=id).all()
    if query:
        actor = query[0]
        return render_template("actors/edit.html", actor=actor)
    else:
        return render_template("actors/index.html")


@actors_blueprint.route("/actors/<id>/edit", methods=["POST"])
def update(id):
    actor = Actor.query.get(id)
    try:
        name = (request.form.get("name"),)
        uid = (request.form.get("uid"),)
        filmography_movie_url = (request.form.get("filmography_movie_url"),)
        filmography_movie_title = request.form.get("filmography_movie_title")
        actor.name = name[0]
        actor.uid = uid[0]
        actor.filmography_movie_title = filmography_movie_title[0]
        actor.filmography_movie_url = filmography_movie_url[0]

        db.session.flush()
        db.session.commit()
    except AssertionError as errors:
        return render_template("actors/edit.html", errors=errors)

    return redirect("/actors")


@actors_blueprint.route("/actors/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        flash("No file part")
        return render_template("/upload/index.html")
    file = request.files["file"]
    if file and allowed_file(file.filename):
        for row in file.readlines():
            temp = json.loads(row)
            actor = Actor()
            actor.name = temp.get("name")
            actor.uid = temp.get("uid")
            actor.filmography_movie_url = str(temp.get("filmography_movie_url"))
            actor.filmography_movie_title = str(temp.get("filmography_movie_title"))

            db.session.add(actor)
        db.session.flush()
        db.session.commit()

        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        print(file)
        # ipdb.set_trace()
        flash("Successfully uploaded file")
    else:
        flash("Unallowed file type")
    return render_template("/upload/index.html")
