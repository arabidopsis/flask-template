from __future__ import annotations

# pylint: disable=line-too-long
CDN = {
    "bootstrap_select": {  # not used now
        "js": {
            "src": "https://cdn.jsdelivr.net/npm/bootstrap-select@1.13.12/dist/js/bootstrap-select.min.js",
            "integrity": "sha256-+o/X+QCcfTkES5MroTdNL5zrLNGb3i4dYdWPWuq6whY=",
            # "src": "https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.13.18/js/bootstrap-select.min.js",
            # "integrity": "sha512-yDlE7vpGDP7o2eftkCiPZ+yuUyEcaBwoJoIhdXv71KZWugFqEphIS3PU60lEkFaz8RxaVsMpSvQxMBaKVwA5xg==",
        },
        "css": {
            "href": "https://cdn.jsdelivr.net/npm/bootstrap-select@1.13.12/dist/css/bootstrap-select.min.css",
            "integrity": "sha256-l3FykDBm9+58ZcJJtzcFvWjBZNJO40HmvebhpHXEhC0=",
            # "href": "https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.13.18/css/bootstrap-select.min.css",
            # "integrity": "sha512-ARJR74swou2y0Q2V9k0GbzQ/5vJ2RBSoCWokg4zkfM29Fb3vZEQyv0iWBMW/yvKgyHSR/7D64pFMmU8nYmbRkg==",
        },
    },
    "toastr": {  # at 2.1.4
        "js": {
            "src": "https://cdnjs.cloudflare.com/ajax/libs/toastr.js/2.1.4/toastr.min.js",
            "integrity": "sha256-yNbKY1y6h2rbVcQtf0b8lq4a+xpktyFc3pSYoGAY1qQ=",
        },
        "css": {
            "href": "https://cdnjs.cloudflare.com/ajax/libs/toastr.js/2.1.4/toastr.min.css",
            "integrity": "sha256-R91pD48xW+oHbpJYGn5xR0Q7tMhH4xOrWn1QqMRINtA=",
        },
    },
    "nunjucks": {  # at 3.0.1
        "js": {
            "src": "https://cdnjs.cloudflare.com/ajax/libs/nunjucks/3.0.1/nunjucks.min.js",
            "integrity": "sha256-sh9FYQZVVLprCQB3/IcNyCRrZwu9hZ+xLHhUszDfsK4=",
        },
    },
    "select2": {  # at 4.0.13
        "js": {
            "src": "https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.12/js/select2.min.js",
            "integrity": "sha256-wfVTTtJ2oeqlexBsfa3MmUoB77wDNRPqT1Q1WA2MMn4=",
        },
        "css": {
            "href": "https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.12/css/select2.min.css",
            "integrity": "sha256-FdatTf20PQr/rWg+cAKfl6j4/IY3oohFAJ7gVC3M34E=",
        },
    },
    "select2_bootstrap": {
        "css": {
            # "href": "https://cdnjs.cloudflare.com/ajax/libs/select2-bootstrap-theme/0.1.0-beta.10/select2-bootstrap.min.css",
            # "integrity": "sha256-nbyata2PJRjImhByQzik2ot6gSHSU4Cqdz5bNYL2zcU=",
            "href": "https://cdn.jsdelivr.net/npm/@ttskch/select2-bootstrap4-theme@1.4.0/dist/select2-bootstrap4.min.css",
            "integrity": "sha256-3UPl0A8ykc7qW77XmHP0HDb1Nvs/09AACcTrNpIbdJ4=",
        },
    },
    "jquery": {
        "js": {
            # "src": "https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js",
            # "integrity": "sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=",
            "src": "https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js",
            "integrity": "sha512-bLT0Qm9VnAYZDflyKcBaQ2gg0hSYNQrJ8RilYldYQ1FxQYoCLtUjuuRuZo+fjqhx/qtq/1itJ0C2ejDxltZVFg==",
        },
    },
    "bootstrap": {
        "css": dict(
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css",
            integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x",
        ),
        "js": dict(
            src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js",
            integrity="sha384-gtEjrD/SeCtmISkJkNUaaKMoLD0//ElJ19smozuHV6z3Iehds+3Ulb9Bn9Plx0x4",
        ),
    },
    "fontawesome": {
        "js": {
            # "src": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.12.1/js/all.min.js",
            # "integrity": "sha256-MAgcygDRahs+F/Nk5Vz387whB4kSK9NXlDN3w58LLq0=",
            "src": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/js/all.min.js",
            "integrity": "sha512-YSdqvJoZr83hj76AIVdOcvLWYMWzy6sJyIMic2aQz5kh2bPTd9dzY3NtdeEAzPp/PhgZqr4aJObB3ym/vsItMg==",
        },
        "css": {
            # "href": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.12.1/css/all.min.css",
            # "integrity": "sha256-mmgLkCYLUQbXn0B1SRqzHar6dCnv9oZFPEC1g1cwlkk=",
            "href": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css",
            "integrity": "sha512-1PKOgIY59xJ8Co8+NE6FZ+LOAZKjy+KY8iq0G4B3CyeY6wYHN3yt9PW0XpSriVlkMXe40PTKnXrLnZ9+fkDaog==",
        },
    },
    "popper": {
        "js": {
            # "src": "https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js",
            # "integrity": "sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49",
            # doesn't work
            # "src": "https://cdnjs.cloudflare.com/ajax/libs/popper.js/2.4.4/umd/popper.min.js",
            # "integrity": "sha512-eUQ9hGdLjBjY3F41CScH3UX+4JDSI9zXeroz7hJ+RteoCaY+GP/LDoM8AO+Pt+DRFw3nXqsjh9Zsts8hnYv8/A==",
            # from bootstrap site
            "src": "https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js",
            "integrity": "sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN",
        },
    },
    "mathjax": {
        "js": {
            "src": "https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.1.0/es5/mml-chtml.min.js",
            "integrity": "sha512-ftLl5l2YVXWQ8sZP+SGWF89QOV4qrUsIxYngipCglbnV2Y9bOy0iliMm2hktG/o+R8+FGWnSdXa7lS4kkY4nIQ==",
            "async": True,
        },
    },
    "requirejs": {
        "js": {
            "src": "https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js",
            "integrity": "sha256-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=",
        },
    },
}
