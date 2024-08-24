from __future__ import annotations

import logging
import os
import sys
import time
from logging import Formatter
from logging import getLogger
from logging import StreamHandler
from logging.handlers import RotatingFileHandler
from logging.handlers import SMTPHandler

from flask import Flask
from flask import has_request_context
from flask import request


def remote_addr() -> str | None:
    # try CloudFlare
    addr = request.headers.get("CF-Connecting-IP")
    if addr:
        return addr
    addr = request.headers.get("X-Forwarded-For")
    if addr:
        return addr
    return request.remote_addr


def escapeit(url: str | None) -> str:
    # because microsoft mangles urls
    if not url:
        return ""
    return url.replace("https://", "").replace("http://", "")


class RequestFormatter(Formatter):
    def format(self, record: logging.LogRecord) -> str:
        ret = super().format(record)
        if not has_request_context():
            return ret

        extra = """
Remote Address:       {remote_addr}
Request Path:         {req.path}
Request Values:       {req.values}
Request User-Agent:   {req.user_agent}
Original Referrer:    {oref}
Request Referrer:     {req.referrer}

""".format(
            req=request,
            remote_addr=remote_addr(),
            oref=escapeit(request.referrer),
        )
        return extra + ret


class LimitFilter(logging.Filter):
    def __init__(self, delay: int = 60 * 5):
        super().__init__("")
        self.start = time.time()
        self.delay = delay

    def filter(self, record: logging.LogRecord) -> bool:
        t = time.time()
        if (t - self.start) > self.delay:
            self.start = t
            return True
        return False


def init_logger(app: Flask, Cls: type[SMTPHandler] = SMTPHandler) -> None:
    logdir: str | None = app.config.get("LOGDIR", None)
    handler: logging.Handler | None = None
    if logdir is not None:
        path = (
            os.path.join(app.instance_path, logdir)
            if not os.path.isabs(logdir)
            else logdir
        )
        if os.path.isdir(path) and os.access(path, os.W_OK | os.X_OK):
            handler = RotatingFileHandler(
                os.path.join(path, app.name + ".log"),
                maxBytes=50000000,
                backupCount=5,
            )

    if handler is None:
        handler = StreamHandler(sys.stderr)

    handler.setLevel(logging.WARNING)
    handler.setFormatter(
        Formatter(
            "%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]",
        ),
    )

    app.logger.addHandler(handler)

    admins = app.config.get("ADMINS")
    if not admins:
        return
    if isinstance(admins, str):
        admins = [admins]
    ext = admins[0].rsplit("@", maxsplit=1)[0]
    name = app.config.get("MAIL_SUBJECT_LINE", app.name)
    mailhost = app.config.get("MAIL_SERVER", "localhost")
    if isinstance(mailhost, str) and ":" in mailhost:
        mailhost = mailhost.split(":")
        mailhost = (mailhost[0], int(mailhost[1]))
    mail_handler = Cls(
        mailhost,
        app.name + f"-server-error@{ext}",
        admins,
        subject=name + " Failed",
    )

    mail_handler.setLevel(logging.ERROR)

    delay = app.config.get("LOG_ERROR_DELAY")

    if delay is not None and delay > 0:
        mail_handler.addFilter(LimitFilter(delay=delay))
    mail_handler.setFormatter(
        RequestFormatter(
            """
Message type:       %(levelname)s
Location:           %(pathname)s:%(lineno)d
Module:             %(module)s
Function:           %(funcName)s
Time:               %(asctime)s

Message:

%(message)s
""",
        ),
    )

    app.logger.addHandler(mail_handler)


def test_logger():
    """Test if the error logger will actually send an email on an error"""
    import platform
    from .flask_utils import create_and_config

    config = create_and_config()
    if "MAIL_SERVER " not in config:
        print("no MAIL_SERVER configured; where is the SMTP server?")
        return
    if "ADMINS " not in config:
        print("no ADMINS configured; who will in send the email to?")
        return
    MAIL_SERVER = config["MAIL_SERVER"]
    ADMINS = config["ADMINS"]
    if isinstance(ADMINS, str):
        ADMINS = [ADMINS]
    if not ADMINS:
        print("no ADMINS configured; who will in send the email to?")
        return
    ext = ADMINS[0].rsplit("@", maxsplit=1)[0]
    whoami = config.get("WHOAMI", f"server-error@{ext}")
    mail_handler = SMTPHandler(
        MAIL_SERVER,
        whoami,
        ADMINS,
        subject=f"A test  error email from: {__file__}",
    )

    mail_handler.setLevel(logging.ERROR)
    logger = getLogger("emma")
    logger.addHandler(mail_handler)
    print(f"sending via {MAIL_SERVER} to {ADMINS}")
    logger.error(
        "this is an error from %s (%s) from code: %s",
        MAIL_SERVER,
        platform.node(),
        __file__,
    )


if __name__ == "__main__":
    test_logger()
