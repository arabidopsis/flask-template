from __future__ import annotations

from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

from .flask_utils import config_app
from .flask_utils import register_bytecode_cache
from .flask_utils import register_filters
from .utils import git_version


def create_app() -> Flask:
    app = create_init_app()
    init_full_app(app)
    return app


def create_init_app() -> Flask:
    app = Flask(
        "app",
        instance_relative_config=True,
        template_folder="templates",
    )
    # config_app is available to celery worker and celery beat
    # so they can configure themselves properly too
    config_app(app.config)

    app.config["GIT_VERSION"] = git_version() or ""
    if app.debug:
        # avoid caching ...
        app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

    if app.config.get("PROXY_FIX", False):
        app.wsgi_app = ProxyFix(app.wsgi_app)  # type: ignore[assignment]

    return app


def init_full_app(app: Flask) -> None:
    # pylint: disable=reimported
    from .logger import init_logger

    init_logger(app)

    from .main_view import init_app

    init_app(app)

    # init_login(app)

    register_filters(app)

    register_bytecode_cache(app)


def init_login(app: Flask) -> None:

    from .login.login_view import init_app

    init_app(app)
