from __future__ import annotations

from flask import Blueprint
from flask import current_app
from flask import Flask
from flask import render_template


view = Blueprint("view", __name__)


@view.route("/")
def index():
    return render_template(
        "base.html",
    )


@view.route("/favicon.ico")
def favicon():
    return current_app.send_static_file("favicon.ico")


def init_app(app: Flask, url_prefix: str = "/") -> None:
    app.register_blueprint(view, url_prefix=url_prefix)
