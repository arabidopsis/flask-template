from __future__ import annotations

APP_NAME = "My Application"
# for meta tags
APP_SUMMARY = APP_NAME
URL = "https://some.website"

BASE_TEMPLATE = "base.html"

VERSION = 1
FONT_ICONS = True

ICON = "img/flask.webp"

MESSAGE = """
Pretty minimal template to get started with a flask website.
Feel free to hack and delete your copy of it.
"""

# create an SMTP logger for
# all unhandled server errors (e.g. 500) will
# send an email to ADMINS
# MAIL_SERVER # SMTP mailserver
# ADMINS: list[str] # list of emails
