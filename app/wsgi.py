from __future__ import annotations

from .app import create_app

# entrypoint for -- say -- gunicorn or flask e.g.
# export FLASK_APP=plantenergy_web.wsgi
# flask run
application = create_app()

del create_app
