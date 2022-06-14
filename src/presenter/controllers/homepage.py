from flask import Flask, Blueprint, jsonify, render_template, url_for, request, redirect

home_blueprint = Blueprint("home", __name__)

from presenter.app import app, db


@home_blueprint.route("/home")
def index():
    return render_template("homepage/index.html")
