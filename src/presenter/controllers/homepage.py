from flask import Flask, Blueprint, jsonify, render_template, url_for, request, redirect

home_blueprint = Blueprint("home", __name__)

from presenter.app import app, db
from presenter.services.search import Search


@home_blueprint.route("/")
def index():
    search_string = request.args.get("q", "")
    service = Search()
    search_result = service.paginated_search(query=search_string)
    return render_template(
        "/homepage/index.html",
        movies=search_result["movies"],
        actors=search_result["actors"],
        query=search_string,
        current_page=search_result["current_page"],
        items_per_page=search_result["per_page"],
        movie_mess=search_result["movie_mess"],
        actors_mess=search_result["actors_mess"],
    )


@home_blueprint.route("/upload")
def upload_file():
    return render_template("/upload/index.html")
