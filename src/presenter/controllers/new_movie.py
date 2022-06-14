from flask import Flask, Blueprint, jsonify, render_template, url_for, request, redirect

newmovie_blueprint = Blueprint("newmovie", __name__)

from presenter.app import app, db
from presenter.models.movie import Movie


@newmovie_blueprint.route("/movies/newmovie")
def index():
    return render_template("movies/new.html")


@newmovie_blueprint.route("/movies/newmovie", methods=["POST"])
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

        errors = movie.errors
        db.session.add(movie)
        db.session.commit()
    except AssertionError as e:
        errors = e
        return render_template("movies/new.html", errors=errors)

    return redirect("/movies")
