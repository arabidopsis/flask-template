# Login Blueprint

This is the simplest way I know to password
protect a website. It requires Flask-Login.

It has a set of public endpoints that include
`login.login_cmd` and `static`. You can add to this
with  `PUBLIC_ENDPOINTS` as a list of other endpoints
to whitelist.

The "database" in this case is just either a single
`password` or a dictionary of `email` => `password`
as spcified by `SITE_PASSWORD` configuration variable.
You can of course improve on this... :)

Just ensure that you call `init_app` in `login_view.py`
when creating your app (see `app.init_fg_app`).

Of course if you don't need any of this just delete this directory;
There is no dependency in the main app.
