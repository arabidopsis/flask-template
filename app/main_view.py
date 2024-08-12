from __future__ import annotations

from flask import Blueprint
from flask import Flask
from flask import render_template
from flask import send_from_directory


view = Blueprint("view", __name__)


@view.route("/")
def index():
    return render_template(
        "raw.html",
    )


@view.route("/favicon.ico")
def favicon():
    return send_from_directory("static", "favicon.ico")


def init_app(app: Flask, url_prefix: str = "/") -> None:
    app.register_blueprint(view, url_prefix=url_prefix)
