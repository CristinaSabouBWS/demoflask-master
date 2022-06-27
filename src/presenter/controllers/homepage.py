from flask import Flask, Blueprint, jsonify, render_template, url_for, request, redirect

home_blueprint = Blueprint("home", __name__)

from presenter.app import app, db
from presenter.services.search import Search


@home_blueprint.route("/")
def index():
    search_string = request.args.get("q", "")
    # per_page = request.args.get("items", 5, type=int)
    # current_page = request.args.get("page", 1, type=int)

    service = Search()
    search_result = service.paginated_search(query=search_string)
    movie_result = search_result["movies"]
    actors_result = search_result["actors"]
    current_page = search_result["current_page"]
    per_page = search_result["per_page"]
    mess = ""
    return render_template(
        "/homepage/index.html",
        movies=movie_result,
        actors=actors_result,
        query=search_string,
        current_page=current_page,
        items_per_page=per_page,
        mess=mess,
    )


@home_blueprint.route("/upload")
def upload_file():
    return render_template("/upload/index.html")
