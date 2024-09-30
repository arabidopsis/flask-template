from __future__ import annotations

import gzip
import os
import tomllib
from datetime import datetime
from os.path import abspath
from os.path import join
from os.path import normpath
from pathlib import Path
from random import random
from typing import Any
from typing import Iterator

from flask import current_app
from flask import Flask
from flask import render_template
from flask import Response
from flask import stream_with_context
from flask import url_for
from flask.config import Config
from flask.sansio.scaffold import find_package
from jinja2 import FileSystemBytecodeCache
from jinja2 import FileSystemLoader
from jinja2 import TemplateNotFound
from markupsafe import Markup

from .utils import attrstr
from .utils import human

NAME = __name__.split(".", maxsplit=1)[0]


def error_resp(msg: str, code: int) -> Response:
    return Response(msg, code, mimetype="text/plain")


def stream_template(template_name: str, **context) -> Response:
    current_app.update_template_context(context)
    template = current_app.jinja_env.get_template(template_name)
    rv = template.stream(context)
    # rv.disable_buffering()
    rv.enable_buffering(5)
    return Response(stream_with_context(rv))


def auto_find_instance_path(name: str = NAME) -> str:
    # cut'n'paste from flask
    prefix, package_path = find_package(name)
    if prefix is None:
        return join(package_path, "instance")
    return join(prefix, "var", f"{name}-instance")


def init_config(name: str = NAME) -> Config:
    # assumes that instance_relative_config=True is set for Flask app too
    instance_path = normpath(abspath(auto_find_instance_path(name)))
    return Config(instance_path)


def dedottify(d: dict[str, Any]) -> dict[str, Any]:
    ret = {}
    for k, v in d.items():
        if isinstance(v, dict):
            v = dedottify(v)
        if "." not in k:
            ret[k] = v
        else:
            *path, k = k.split(".")
            d = ret
            for p in path:
                if p in d:
                    d = d[p]
                    assert isinstance(d, dict)
                else:
                    o: dict[str, Any] = {}
                    d[p] = o
                    d = o
            d[k] = v
    return ret


def merge_dict(d1: dict, d2: dict) -> dict:
    for k, v2 in dedottify(d2).items():
        if k not in d1:
            d1[k] = v2
        else:
            v1 = d1[k]
            if isinstance(v1, dict) and isinstance(v2, dict):
                d1[k] = merge_dict(v1, v2)
            else:
                d1[k] = v2  # overwrite with v2

    return d1


def config_app(config: Config) -> Config:
    config.from_object(f"{NAME}.config")
    config.from_pyfile(f"{NAME}.cfg", silent=True)

    return config


def create_and_config(name: str = NAME) -> Config:
    return config_app(init_config(name))


def register_bytecode_cache(app: Flask, directory="bytecode_cache") -> None:
    if not os.path.isabs(directory):
        cache = os.path.join(app.instance_path, directory)
    else:
        cache = directory
    if not os.path.isdir(cache):
        os.makedirs(cache, exist_ok=True)
    app.jinja_options.update(
        {"bytecode_cache": FileSystemBytecodeCache(cache)},
    )


def register_filters(app: Flask) -> None:
    """Register page not found filters."""

    # from .cdn import CDN
    with open(join(app.root_path, "cdn.toml"), "rb") as fp:
        CDN = tomllib.load(fp)

    def include_raw(filename: str) -> Markup:
        def markup(loader: FileSystemLoader | None) -> Markup | None:
            if loader is None:
                return None
            for path in loader.searchpath:
                f = Path(path).joinpath(filename)
                if f.is_file():
                    with gzip.open(f, "rt", encoding="utf8") as fp:
                        return Markup(fp.read())
            return None

        def get_loaders() -> Iterator[FileSystemLoader]:
            loader = app.jinja_loader
            if isinstance(loader, FileSystemLoader):
                yield loader

            for blueprint in app.iter_blueprints():
                loader = blueprint.jinja_loader
                if isinstance(loader, FileSystemLoader):
                    yield loader

        if filename.endswith((".gz", ".svgz")):
            for loader in get_loaders():
                ret = markup(loader)
                if ret is not None:
                    return ret
            raise TemplateNotFound(filename)

        ldr = app.jinja_env.loader
        if ldr is None:
            raise TemplateNotFound(filename)
        src = ldr.get_source(app.jinja_env, filename)[0]
        return Markup(src)

    def cdn_js(key, **kwargs):
        js = CDN[key]["js"]
        args = {k: v for k, v in js.items() if k not in ["integrity", "src"]}
        args.update(kwargs)
        args.setdefault("crossorigin", "anonymous")
        args.setdefault("referrerpolicy", "no-referer")
        attrs = attrstr(args)
        integrity = js.get("integrity")
        integrity = f'integrity="{integrity}"' if integrity else ""

        return Markup(
            f"""<script src="{js['src']}"
            {integrity} {attrs}></script>""",
        )

    def cdn_css(key, **kwargs):
        css = CDN[key]["css"]
        args = {k: v for k, v in css.items() if k not in ["integrity", "href", "rel"]}
        args.update(kwargs)
        args.setdefault("crossorigin", "anonymous")
        args.setdefault("referrerpolicy", "no-referer")
        attrs = attrstr(args)
        integrity = css.get("integrity")
        integrity = f'integrity="{integrity}"' if integrity else ""
        return Markup(
            f"""<link rel="stylesheet" href="{css['href']}"
            {integrity} {attrs}>""",
        )

    def static_js(filename: str, endpoint: str = "static", **kwargs: Any) -> Markup:
        attrs = attrstr(kwargs)
        url = url_for(endpoint, filename=f"js/{filename}", **getversion())
        return Markup(f'<script src="{url}" {attrs}></script>')

    def static_css(filename: str, endpoint: str = "static", **kwargs: Any) -> Markup:
        attrs = attrstr(kwargs)
        url = url_for(endpoint, filename=f"css/{filename}", **getversion())
        return Markup(f'<link rel="stylesheet" href="{url}" {attrs}>')

    # for cache busting js and css files
    # e.g. url_for('static', filename='js/myjs.js', **getversion())
    version = app.config["VERSION"]
    if app.debug:

        def getversion():
            return {"v": f"v{random()}"}

    else:

        def getversion():
            return {"v": version}

    app.jinja_env.globals["include_raw"] = include_raw
    app.jinja_env.globals["cdn_js"] = cdn_js
    app.jinja_env.globals["cdn_css"] = cdn_css
    app.jinja_env.globals["static_js"] = static_js
    app.jinja_env.globals["static_css"] = static_css
    app.jinja_env.globals["year"] = datetime.now().year
    app.jinja_env.globals["base_template"] = app.config["BASE_TEMPLATE"]
    app.jinja_env.globals["getversion"] = getversion

    app.template_filter("human")(human)

    @app.template_filter()
    def split(s, sep=None):  # pylint: disable=unused-variable
        return [] if not s else (s.split(sep) if sep is not None else s.split())

    @app.errorhandler(404)
    def page_not_found(e):  # pylint: disable=unused-variable
        return render_template("errors/404.html"), 404
