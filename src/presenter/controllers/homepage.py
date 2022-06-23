from flask import Flask, Blueprint, jsonify, render_template, url_for, request, redirect


home_blueprint = Blueprint("home", __name__)
from presenter.services.search_service import Search


@home_blueprint.route("/")
def index():
    service = SearchService()
    results = service.search(request.args("q"))
    results = []
    return render_template("homepage/index.html", results=results)
