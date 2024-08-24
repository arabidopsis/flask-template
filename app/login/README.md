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
