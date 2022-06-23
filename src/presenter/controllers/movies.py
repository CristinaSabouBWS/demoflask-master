from flask import Flask, Blueprint, jsonify, render_template, url_for, request, redirect, flash
from werkzeug.utils import secure_filename
import os


movies_blueprint = Blueprint("movies", __name__)


import ipdb
import json
from presenter.app import ALLOWED_EXTENSIONS, UPLOAD_FOLDER

from presenter.models.movie import Movie


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@movies_blueprint.route("/movies/")
def index():
    all_movies = Movie.query.order_by(Movie.id).all()
    per_page = request.args.get("items", 5, type=int)
    current_page = request.args.get("page", 1, type=int)

    movie_count = len(all_movies)

    start = per_page * (current_page - 1)
    end = min(start + per_page, movie_count)
    movies = all_movies[start:end]
    mess = ""
    if len(movies) == 0:
        mess = "Error message, no more items"

    return render_template(
        "movies/index.html", movies=movies, current_page=current_page, items_per_page=per_page, mess=mess
    )


def to_list(dbstring):
    dbstring = dbstring.strip("][")
    li = dbstring.split(", ")
    result = []
    for item in li:
        result.append((item[1:-1]))
    return result


@movies_blueprint.route("/movies/<id>")
def show(id):
    query = Movie.query.filter_by(id=id).all()
    if query:
        movie = query[0]
        actors = to_list(movie.top_cast)
        print(movie.top_cast)
        return render_template("movies/movie.html", movie=movie, actors=actors)
    else:
        return render_template("movies/index.html")


@movies_blueprint.route("/movies/new")
def new():
    return render_template("movies/new.html")


@movies_blueprint.route("/movies/new", methods=["POST"])
def create():
    try:
        movie = Movie(
            genre=request.form.get("genre"),
            date_of_scraping=request.form.get("date_of_scraping"),
            directors=request.form.get("directors"),
            title=request.form.get("title"),
            rating=request.form.get("rating"),
            release_year=request.form.get("release_year"),
            top_cast=request.form.get("top_cast"),
            url=request.form.get("url"),
            uid=request.form.get("uid"),
            image_url=request.form.get("image_url"),
            image_path=request.form.get("image_path"),
        )

        db.session.add(movie)
        db.session.commit()
    except AssertionError as errors:
        return render_template("movies/new.html", errors=errors)

    return redirect("/movies")


@movies_blueprint.route("/movies/<id>/edit")
def edit(id):
    query = Movie.query.filter_by(id=id).all()
    if query:
        movie = query[0]
        return render_template("movies/edit.html", movie=movie)
    else:
        return render_template("movies/index.html")


@movies_blueprint.route("/movies/<id>/edit", methods=["POST"])
def update(id):
    movie = Movie.query.get(id)
    try:
        # ipdb.set_trace()
        genre = (request.form.get("genre"),)
        date_of_scraping = (request.form.get("date_of_scraping"),)
        directors = (request.form.get("directors"),)
        title = (request.form.get("title"),)
        rating = (request.form.get("rating"),)
        release_year = (request.form.get("release_year"),)
        top_cast = (request.form.get("top_cast"),)
        url = (request.form.get("url"),)
        uid = (request.form.get("uid"),)
        image_url = (request.form.get("image_url"),)
        image_path = request.form.get("image_path")

        movie.genre = genre[0]
        movie.date_of_scraping = date_of_scraping[0]
        movie.directors = directors[0]
        movie.title = title[0]
        movie.rating = rating[0]
        movie.release_year = release_year[0]
        movie.top_cast = top_cast[0]
        movie.url = url[0]
        movie.uid = uid[0]
        movie.image_url = image_url[0]
        movie.image_path = image_path[0]

        db.session.flush()
        db.session.commit()
    except AssertionError as errors:
        return render_template("movies/edit.html", errors=errors)

    return redirect("/movies")


@movies_blueprint.route("/upload")
def upload_file():
    return render_template("/upload/index.html")


@movies_blueprint.route("/movies/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        flash("No file part")
        return render_template("/upload/index.html")
    file = request.files["file"]
    if file and allowed_file(file.filename):
        for row in file.readlines():
            temp = json.loads(row)
            movie = Movie()
            movie.title = temp.get("title")
            movie.uid = temp.get("uid")
            movie.url = temp.get("url")
            movie.genre = str(temp.get("genre"))
            movie.directors = str(temp.get("directors"))
            movie.date_of_scraping = str(temp.get("date_of_scraping"))
            movie.rating = temp.get("rating")
            # movie.release_year = int(temp.get("release_year"))
            movie.top_cast = str(temp.get("top_cast"))
            # movie.image_url = temp.get("image_url")
            # movie.image_path = str(temp.get("image_path"))

            db.session.add(movie)
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
