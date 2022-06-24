from flask import Flask, Blueprint, jsonify, render_template, url_for, request, redirect

home_blueprint = Blueprint("home", __name__)

from presenter.app import app, db
from presenter.services.search import Search


@home_blueprint.route("/")
def index():

    search_string = request.args.get("q", "")
    service = Search()
    search_result = service.search(search_string)

    movie_result = search_result["movies"]
    actors_result = search_result["actors"]
    per_page = request.args.get("items", 10, type=int)
    current_page = request.args.get("page", 1, type=int)

    # movies_count = len(movie_result)
    # actors_count = len(actors_result)
    # start = per_page * (current_page - 1)
    # movie_end = min(start + per_page, movie_count)
    # actors_end = min(start + per_page, actors_count)
    # movies = search_result[start:movie_end]
    # actors = search_result[start:actors_end]
    mess = ""
    # if len(search_result) == 0:
    #     mess = f"Nothing was found for {search_string} "
    # elif len(movies) == 0:
    #     mess = "No more items"

    return render_template(
        "homepage/index.html",
        movies=movie_result,
        actors=actors_result,
        query=search_string,
        current_page=current_page,
        items_per_page=per_page,
        mess=mess,
    )
